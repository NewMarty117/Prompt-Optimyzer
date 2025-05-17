import gradio as gr
import json
import os
import sys
import pandas as pd
import pyperclip # For copy to clipboard

# --- Path Setup ---
APP_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP_ROOT_DIR) # Add project root to path

# --- Project Modules ---
from app.utils.translator import translate_to_english
from app.core.llm_connector import call_lm_studio, call_gemini_api
from app.core.prompt_optimizer import PromptOptimizer
from app.core.batch_processor import process_batch_file
from app.core.prompt_evaluator import PromptEvaluator
from app.utils.feedback_manager import save_feedback
from app.utils.exporter import export_data, load_history, add_to_history, MAX_HISTORY_ITEMS

CONFIG_FILE = os.path.join(APP_ROOT_DIR, "app", "config.json")
LOCALE_DIR = os.path.join(APP_ROOT_DIR, "app", "locales")

# --- Localization ---
current_lang = "fr"  # Default language
translations = {}

def load_translations(lang_code="fr"):
    global translations, current_lang
    current_lang = lang_code
    try:
        file_path = os.path.join(LOCALE_DIR, f"{lang_code}.json")
        with open(file_path, "r", encoding="utf-8") as f:
            translations = json.load(f)
    except FileNotFoundError:
        print(f"Error: Language file {lang_code}.json not found. Defaulting to English.")
        if lang_code != "en":
            load_translations("en")
        else:
            translations = {}
    except json.JSONDecodeError:
        print(f"Error decoding {lang_code}.json. Using empty translations.")
        translations = {}

def _(key, **kwargs):
    return translations.get(key, key).format(**kwargs)

load_translations(current_lang)

# --- Configuration Functions ---
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"google_gemini_api_key": ""}
    return {"google_gemini_api_key": ""}

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

config_data = load_config()
prompt_optimizer_instance = PromptOptimizer()
prompt_evaluator_instance = PromptEvaluator()

def update_gemini_api_key(api_key, lang):
    load_translations(lang)
    config_data["google_gemini_api_key"] = api_key
    save_config(config_data)
    label_key = "gemini_api_key_label_saved" if api_key else "gemini_api_key_label"
    status_key = "api_key_saved_status" if api_key else "api_key_removed_status"
    return gr.update(label=_(label_key), value=api_key), _(status_key)

# --- Main Processing Logic (single prompt) ---
def process_single_prompt_for_display(original_text, image_model, llm_backend, current_gemini_api_key, detail_level, target_length, visual_style_value, lang):
    load_translations(lang)
    if not original_text.strip():
        return _("error_empty_initial_description"), "0/100", original_text, ""

    llm_instruction_prompt = prompt_optimizer_instance.generate_llm_instruction_prompt(
        user_text=original_text,
        image_model_name=image_model,
        detail_level=detail_level,
        target_length=target_length,
        visual_style_value=visual_style_value
    )

    if llm_instruction_prompt.startswith("[Erreur") or llm_instruction_prompt.startswith("[Error"):
        return llm_instruction_prompt, "0/100", original_text, ""

    optimized_prompt_from_llm = ""
    if llm_backend == "LM Studio (local)":
        optimized_prompt_from_llm = call_lm_studio(llm_instruction_prompt)
    elif llm_backend == "Google Gemini Flash 2.0 (API)":
        if not current_gemini_api_key:
            return _("error_gemini_api_key_missing"), "0/100", original_text, ""
        optimized_prompt_from_llm = call_gemini_api(llm_instruction_prompt, api_key=current_gemini_api_key)
    else:
        optimized_prompt_from_llm = _("error_llm_backend_not_recognized")

    error_message_key = None
    if optimized_prompt_from_llm.startswith("["):
        if optimized_prompt_from_llm.startswith("[LM Studio Error: "):
            error_detail = optimized_prompt_from_llm[len("[LM Studio Error: "):-1]
            error_message_key = _("error_lm_studio_connection", error=error_detail)
        elif optimized_prompt_from_llm.startswith("[LM Studio Response Error: "):
            error_message_key = _("error_lm_studio_parsing")
        elif optimized_prompt_from_llm.startswith("[Gemini API Error: "):
            error_detail = optimized_prompt_from_llm[len("[Gemini API Error: "):-1]
            error_message_key = _("error_gemini_api_key_invalid") if "API_KEY_INVALID" in error_detail or "API key not valid" in error_detail else _("error_gemini_api_call", error=error_detail)
        else:
            error_message_key = optimized_prompt_from_llm
        return error_message_key, "0/100", original_text, ""

    final_english_prompt = optimized_prompt_from_llm.strip()
    score_value = prompt_evaluator_instance.evaluate_prompt(final_english_prompt, image_model, detail_level)
    add_to_history(original_text, final_english_prompt, f"{score_value}/100", image_model, llm_backend)
    return final_english_prompt, f"{score_value}/100", original_text, _("copied_to_clipboard_message")

# --- Gradio Interface Builder ---
def build_ui_components(lang_code):
    load_translations(lang_code)

    _data_for_export_single = []
    _data_for_export_batch = []

    with gr.Blocks(title=_("app_title")) as interface_block:
        # Assign Markdown components to variables directly
        app_title_md_component = gr.Markdown(f"# {_('app_title')}")
        current_language_radio = gr.Radio(choices=["fr", "en"], value=lang_code, label="Langue / Language", interactive=True)
        original_prompt_for_feedback = gr.Textbox(visible=False)

        with gr.Row() as settings_row: # This is interface_block.children[3] (index starts at 0)
            with gr.Column(scale=1):
                common_settings_header_md_component = gr.Markdown(f"### {_('common_settings_header')}")
                image_model_selector = gr.Dropdown(label=_("target_image_model_label"), choices=["SDXL", "Stable Diffusion 1.5", "Flux 1.0 dev", "HiDream"], value="SDXL")
                llm_backend_selector = gr.Dropdown(label=_("llm_backend_label"), choices=["LM Studio (local)", "Google Gemini Flash 2.0 (API)"], value="LM Studio (local)")
                current_api_key_val = config_data.get("google_gemini_api_key", "")
                gemini_api_key_textbox = gr.Textbox(
                    label=_("gemini_api_key_label") if not current_api_key_val else _("gemini_api_key_label_saved"),
                    value=current_api_key_val, type="password", placeholder=_("gemini_api_key_placeholder"), interactive=True)
                api_key_status_message = gr.Markdown("")
            with gr.Column(scale=1):
                advanced_controls_header_md_component = gr.Markdown(f"### {_('advanced_controls_header')}")
                detail_level_slider = gr.Slider(minimum=1, maximum=10, value=5, step=1, label=_("detail_level_label"))
                prompt_length_slider = gr.Slider(minimum=20, maximum=300, value=75, step=10, label=_("prompt_length_label"))
                visual_style_slider = gr.Slider(minimum=0, maximum=1, value=0.5, step=0.1, label=_("visual_style_label"))

        with gr.Tabs() as tabs_main: # This is interface_block.children[4]
            with gr.TabItem(_("single_optimization_tab"), id="single_opt_tab") as single_opt_tab_item:
                with gr.Row():
                    with gr.Column(scale=2):
                        describe_scene_header_md_component = gr.Markdown(f"## {_('describe_scene_header')}")
                        user_input_text_single = gr.Textbox(label=_("natural_language_input_label"), placeholder=_("natural_language_input_placeholder"), lines=3)
                        submit_button_single = gr.Button(_("optimize_prompt_button"))
                    with gr.Column(scale=1):
                        optimized_prompt_header_md_component = gr.Markdown(f"## {_('optimized_prompt_header')}")
                        optimized_prompt_output_single = gr.Textbox(label=_("optimized_prompt_label"), lines=8, interactive=False)
                        copy_clipboard_button_single = gr.Button(_("copy_to_clipboard_button"))
                        clipboard_status_single = gr.Markdown("")
                        evaluation_score_header_md_component = gr.Markdown(f"## {_('evaluation_score_header')}")
                        prompt_score_output_single = gr.Textbox(label=_("evaluation_score_label"), interactive=False)

                with gr.Accordion(_("feedback_accordion_header"), open=False) as feedback_accordion_single:
                    user_rating_single = gr.Radio([1, 2, 3, 4, 5], label=_("rating_label"), value=None)
                    user_comment_single = gr.Textbox(label=_("comment_label"), lines=2, placeholder=_("comment_placeholder"))
                    save_feedback_button_single = gr.Button(_("save_feedback_button"))
                    feedback_status_single = gr.Markdown("")

                with gr.Accordion(_("export_options_header"), open=False) as export_accordion_single:
                    export_format_single = gr.Dropdown(choices=["txt", "json", "csv"], label=_("export_format_label"), value="txt")
                    export_button_single = gr.Button(_("export_button"))
                    export_status_single = gr.Markdown("")
                    download_file_single = gr.File(label=_("download_export_label"), interactive=False)

            with gr.TabItem(_("batch_processing_tab"), id="batch_proc_tab") as batch_proc_tab_item:
                batch_import_header_md_component = gr.Markdown(f"## {_('batch_import_header')}")
                file_input_batch = gr.File(label=_("batch_file_label"), file_types=[".txt", ".csv"])
                batch_submit_button = gr.Button(_("batch_submit_button"))
                batch_results_header_md_component = gr.Markdown(f"### {_('batch_results_header')}")
                batch_results_output_df = gr.DataFrame(headers=[_("original_prompt"), _("optimized_prompt_en"), _("score")], wrap=True, interactive=False)
                batch_status_message = gr.Markdown("")
                with gr.Accordion(_("export_options_header"), open=False) as export_accordion_batch:
                    export_format_batch = gr.Dropdown(choices=["txt", "json", "csv"], label=_("export_format_label"), value="csv")
                    export_button_batch = gr.Button(_("export_button"))
                    export_status_batch = gr.Markdown("")
                    download_file_batch = gr.File(label=_("download_export_label"), interactive=False)

            with gr.TabItem(_("history_tab"), id="history_view_tab") as history_view_tab_item:
                prompt_history_header_md_component = gr.Markdown(f"## {_('prompt_history_header', count=MAX_HISTORY_ITEMS)}")
                load_history_button = gr.Button(_("load_history_button"))
                history_df_display = gr.DataFrame(headers=[
                    _("history_timestamp_col"), _("history_original_prompt_col"), _("history_optimized_prompt_col"),
                    _("history_score_col"), _("history_image_model_col"), _("history_llm_backend_col")
                ], wrap=True, interactive=False)

        # --- Event Handlers ---
        gemini_api_key_textbox.submit(fn=update_gemini_api_key, inputs=[gemini_api_key_textbox, current_language_radio], outputs=[gemini_api_key_textbox, api_key_status_message])

        def copy_to_clipboard_action(text_to_copy, lang):
            load_translations(lang)
            try:
                pyperclip.copy(text_to_copy)
                return _("copied_to_clipboard_message")
            except Exception as e:
                print(f"Clipboard error: {e}")
                return _("error_clipboard", error=str(e))

        copy_clipboard_button_single.click(fn=copy_to_clipboard_action, inputs=[optimized_prompt_output_single, current_language_radio], outputs=[clipboard_status_single])

        def handle_save_feedback_single_wrapper(orig_prompt, opt_prompt, score, rating, comment, img_model, llm_bcknd_val, lang):
            load_translations(lang)
            if not opt_prompt or opt_prompt.startswith("["):
                return _("feedback_no_prompt_error")
            if rating is None:
                return _("feedback_no_rating_error")
            return save_feedback(orig_prompt, opt_prompt, score, rating, comment, img_model, llm_bcknd_val)

        save_feedback_button_single.click(fn=handle_save_feedback_single_wrapper, inputs=[
            original_prompt_for_feedback, optimized_prompt_output_single, prompt_score_output_single,
            user_rating_single, user_comment_single, image_model_selector, llm_backend_selector, current_language_radio
        ], outputs=[feedback_status_single])

        def process_single_prompt_and_update_export_data(original_text, image_model, llm_backend, current_gemini_api_key, detail_level, target_length, visual_style_value, lang):
            nonlocal _data_for_export_single
            opt_prompt, score, orig_prompt_for_fb, clipboard_msg = process_single_prompt_for_display(original_text, image_model, llm_backend, current_gemini_api_key, detail_level, target_length, visual_style_value, lang)
            if not opt_prompt.startswith("["):
                 _data_for_export_single = [{
                    "original_prompt": original_text,
                    "optimized_prompt_en": opt_prompt,
                    "score": score,
                    "image_model": image_model,
                    "llm_backend": llm_backend
                }]
            else:
                _data_for_export_single = []
            return opt_prompt, score, orig_prompt_for_fb, clipboard_msg

        submit_button_single.click(fn=process_single_prompt_and_update_export_data, inputs=[
            user_input_text_single, image_model_selector, llm_backend_selector, gemini_api_key_textbox,
            detail_level_slider, prompt_length_slider, visual_style_slider, current_language_radio
        ], outputs=[optimized_prompt_output_single, prompt_score_output_single, original_prompt_for_feedback, clipboard_status_single])

        def handle_export_single(export_format_val, lang):
            nonlocal _data_for_export_single
            load_translations(lang)
            if not _data_for_export_single:
                return _("export_no_data_error"), None
            file_path = export_data(_data_for_export_single, export_format_val, "single_prompt_export")
            if file_path.startswith("["):
                return _("export_error_status", error=file_path), None
            return _("export_success_status", filepath=os.path.basename(file_path)), file_path

        export_button_single.click(fn=handle_export_single, inputs=[export_format_single, current_language_radio], outputs=[export_status_single, download_file_single])

        def process_single_prompt_for_batch_wrapper(original_text, image_model, llm_backend, current_gemini_api_key, detail_level, target_length, visual_style_value, lang):
            opt_prompt, score_str, _, _ = process_single_prompt_for_display(original_text, image_model, llm_backend, current_gemini_api_key, detail_level, target_length, visual_style_value, lang)
            return opt_prompt, score_str

        def handle_batch_processing(batch_file_obj, img_model, llm_bck, gem_api_key, det_level, len_slider, style_slider, lang):
            nonlocal _data_for_export_batch
            load_translations(lang)
            if batch_file_obj is None:
                return pd.DataFrame(columns=[_("original_prompt"), _("optimized_prompt_en"), _("score")]), _("batch_error_no_file"), None

            file_path = batch_file_obj.name
            results_df, error_msg = process_batch_file(
                file_path,
                lambda text: process_single_prompt_for_batch_wrapper(text, img_model, llm_bck, gem_api_key, det_level, len_slider, style_slider, lang)
            )

            if error_msg:
                return pd.DataFrame(columns=[_("original_prompt"), _("optimized_prompt_en"), _("score")]), _("batch_error_processing", error=error_msg), None

            if results_df.empty:
                _data_for_export_batch = []
                return results_df, _("batch_no_results"), None

            _data_for_export_batch = results_df.to_dict(orient="records")
            display_df = results_df.rename(columns={
                "original_text": _("original_prompt"),
                "optimized_prompt": _("optimized_prompt_en"),
                "score": _("score")
            })
            return display_df, _("batch_success_status", count=len(results_df)), None # download_file_batch was an output here, should be None if no file to download immediately

        batch_submit_button.click(fn=handle_batch_processing, inputs=[
            file_input_batch, image_model_selector, llm_backend_selector, gemini_api_key_textbox,
            detail_level_slider, prompt_length_slider, visual_style_slider, current_language_radio
        ], outputs=[batch_results_output_df, batch_status_message, download_file_batch]) # download_file_batch might need to be updated by export

        def handle_export_batch(export_format_val, lang):
            nonlocal _data_for_export_batch
            load_translations(lang)
            if not _data_for_export_batch:
                return _("export_no_data_error"), None
            file_path = export_data(_data_for_export_batch, export_format_val, "batch_prompts_export")
            if file_path.startswith("["):
                return _("export_error_status", error=file_path), None
            return _("export_success_status", filepath=os.path.basename(file_path)), file_path

        export_button_batch.click(fn=handle_export_batch, inputs=[export_format_batch, current_language_radio], outputs=[export_status_batch, download_file_batch])

        def handle_load_history(lang):
            load_translations(lang)
            history_data = load_history()
            if not history_data:
                return pd.DataFrame(columns=[
                    _("history_timestamp_col"), _("history_original_prompt_col"), _("history_optimized_prompt_col"),
                    _("history_score_col"), _("history_image_model_col"), _("history_llm_backend_col")
                ])
            df = pd.DataFrame(history_data)
            expected_cols = ["timestamp", "original_prompt", "optimized_prompt_en", "generated_score", "image_model_target", "llm_backend_used"]
            for col in expected_cols:
                if col not in df.columns:
                    df[col] = "N/A" # Ensure columns exist to prevent KeyError during selection
            df = df[expected_cols] # Select in defined order
            df.columns = [
                _("history_timestamp_col"), _("history_original_prompt_col"), _("history_optimized_prompt_col"),
                _("history_score_col"), _("history_image_model_col"), _("history_llm_backend_col")
            ]
            return df

        load_history_button.click(fn=handle_load_history, inputs=[current_language_radio], outputs=[history_df_display])

        # --- Language Change Handler ---
        def update_all_labels_on_lang_change(lang_code_val):
            load_translations(lang_code_val)

            # Prepare translated strings for Markdown components first
            md_app_title_text = f"# {_('app_title')}"
            md_common_settings_text = f"### {_('common_settings_header')}"
            md_advanced_controls_text = f"### {_('advanced_controls_header')}"
            md_describe_scene_text = f"## {_('describe_scene_header')}"
            md_optimized_prompt_text = f"## {_('optimized_prompt_header')}"
            md_eval_score_text = f"## {_('evaluation_score_header')}"
            md_batch_import_text = f"## {_('batch_import_header')}"
            md_batch_results_text = f"### {_('batch_results_header')}"
            md_prompt_history_text = f"## {_('prompt_history_header', count=MAX_HISTORY_ITEMS)}"

            return (
                gr.update(label=_("Langue / Language")),
                gr.update(label=_("target_image_model_label")),
                gr.update(label=_("llm_backend_label")),
                gr.update(label=_("gemini_api_key_label") if not config_data.get("google_gemini_api_key") else _("gemini_api_key_label_saved"), placeholder=_("gemini_api_key_placeholder")),
                gr.update(label=_("detail_level_label")),
                gr.update(label=_("prompt_length_label")),
                gr.update(label=_("visual_style_label")),
                gr.update(label=_("single_optimization_tab")), # TabItem
                gr.update(label=_("natural_language_input_label"), placeholder=_("natural_language_input_placeholder")),
                gr.update(value=_("optimize_prompt_button")),
                gr.update(label=_("optimized_prompt_label")),
                gr.update(value=_("copy_to_clipboard_button")),
                gr.update(label=_("evaluation_score_label")),
                gr.update(label=_("feedback_accordion_header")), # Accordion
                gr.update(label=_("rating_label")),
                gr.update(label=_("comment_label"), placeholder=_("comment_placeholder")),
                gr.update(value=_("save_feedback_button")),
                gr.update(label=_("export_options_header")), # Accordion
                gr.update(label=_("export_format_label")),
                gr.update(value=_("export_button")),
                gr.update(label=_("download_export_label")),
                gr.update(label=_("batch_processing_tab")), # TabItem
                gr.update(label=_("batch_file_label")),
                gr.update(value=_("batch_submit_button")),
                gr.update(headers=[_("original_prompt"), _("optimized_prompt_en"), _("score")]), # DataFrame
                gr.update(label=_("export_options_header")), # Accordion
                gr.update(label=_("export_format_label")),
                gr.update(value=_("export_button")),
                gr.update(label=_("download_export_label")),
                gr.update(label=_("history_tab")), # TabItem
                gr.update(value=_("load_history_button")),
                gr.update(headers=[ # DataFrame
                    _("history_timestamp_col"), _("history_original_prompt_col"), _("history_optimized_prompt_col"),
                    _("history_score_col"), _("history_image_model_col"), _("history_llm_backend_col")
                ]),
                # Markdown updates (returning new content string)
                gr.update(value=md_app_title_text),
                gr.update(value=md_common_settings_text),
                gr.update(value=md_advanced_controls_text),
                gr.update(value=md_describe_scene_text),
                gr.update(value=md_optimized_prompt_text),
                gr.update(value=md_eval_score_text),
                gr.update(value=md_batch_import_text),
                gr.update(value=md_batch_results_text),
                gr.update(value=md_prompt_history_text),
            )

        # Define all components that will be updated by language change
        # Order must match the tuple returned by update_all_labels_on_lang_change
        components_to_update_on_lang_change = [
            current_language_radio,
            image_model_selector, llm_backend_selector, gemini_api_key_textbox,
            detail_level_slider, prompt_length_slider, visual_style_slider,
            single_opt_tab_item, # TabItem
            user_input_text_single, submit_button_single,
            optimized_prompt_output_single, copy_clipboard_button_single, prompt_score_output_single,
            feedback_accordion_single, # Accordion
            user_rating_single, user_comment_single, save_feedback_button_single,
            export_accordion_single, # Accordion
            export_format_single, export_button_single, download_file_single,
            batch_proc_tab_item, # TabItem
            file_input_batch, batch_submit_button, batch_results_output_df, # DataFrame for headers
            export_accordion_batch, # Accordion (in batch tab)
            export_format_batch, export_button_batch, download_file_batch,
            history_view_tab_item, # TabItem
            load_history_button, history_df_display, # DataFrame for headers
            # Markdown components (referenced by their variable names)
            app_title_md_component,
            common_settings_header_md_component,
            advanced_controls_header_md_component,
            describe_scene_header_md_component,
            optimized_prompt_header_md_component,
            evaluation_score_header_md_component,
            batch_import_header_md_component,
            batch_results_header_md_component,
            prompt_history_header_md_component
        ]

        current_language_radio.change(
            fn=update_all_labels_on_lang_change,
            inputs=[current_language_radio],
            outputs=components_to_update_on_lang_change
        )

    return interface_block

# --- Launch the application ---
if __name__ == "__main__":
    app_ui = build_ui_components(current_lang)
    app_ui.launch(share=False) # Set share=True to get a public link if needed