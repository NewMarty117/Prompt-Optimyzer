# AI Prompt Optimizer

The AI Prompt Optimizer is a powerful application designed to enhance and optimize textual prompts for AI image generation models. This tool helps users create more effective prompts that yield better results with models like SDXL, Stable Diffusion 1.5, Flux 1.0 dev, and HiDream.


![Image](https://github.com/user-attachments/assets/fce20773-b228-446f-8743-7f1398aca358)

## Features

* **Natural Language Input**: Describe your scene in simple terms in any language
* **Automatic Translation**: Enter in any language, receive optimized prompts in English (required by image models)
* **Support for Multiple Image Models**: Optimization for SDXL, Stable Diffusion 1.5, Flux 1.0 dev, or HiDream
* **Flexible LLM Backend Options**:

  * Local processing with LM Studio
  * Cloud processing with Google Gemini Flash 2.0 API
* **Advanced Controls**:

  * Adjust level of detail
  * Control prompt length
  * Visual style slider (raw to professional)
* **Cascade Reasoning**: Model-specific logical optimization
* **Batch Processing**: Import TXT or CSV files containing multiple descriptions
* **Automatic Prompt Evaluation**: Quality scoring system for generated prompts
* **User Feedback System**: Rate and comment on generated prompts
* **Multilingual Interface**: Available in French and English
* **Easy Export Options**: Save results in TXT, JSON, or CSV

## Installation Guide

### Requirements

* Windows 10 64-bit or newer
* Python 3.8 or newer
* Internet connection (for initial setup and when using the Google Gemini API)
* [LM Studio](https://lmstudio.ai/) (optional, for local LLM processing)

### Standard Installation

1. **Download the Application**:

   * Download the latest version from my page
   * Extract the ZIP file to your preferred location

2. **Run the Installation Script**:

   * Open the extracted folder
   * Double-click on `install.bat`
   * Wait for the installation to complete (this will create a virtual environment and install all dependencies)

   
   ![Image](https://github.com/user-attachments/assets/5ed99175-8e98-4817-ae31-84be9990a8bc)

3. **Launch the Application**:

   * Once the installation is complete, double-click on `launcher.bat`
   * The application will open in your default web browser

   
   ![Image](https://github.com/user-attachments/assets/00400ad8-aeed-4983-bb19-db81605bbd0a)

### Manual Installation (Advanced Users)

If you prefer manual installation:

1. Create a virtual environment:
   python -m venv venv

2. Activate the virtual environment:
   venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Launch the application:
   python app.py

## LM Studio Configuration for Local Processing

For local LLM processing without relying on external APIs, you can use LM Studio:

1. **Download and Install LM Studio**:

* Download from [lmstudio.ai](https://lmstudio.ai/)
* Follow the installation instructions

   
   ![Image](https://github.com/user-attachments/assets/c2143d38-6e1d-476a-9a7f-fcf4a546a202)

2. **Download a Compatible Model**:

* Open LM Studio
* Go to the "Models" tab
* Download a model suitable for text generation (recommended: Mistral 7B, Llama 2, or similar)

   
   ![Image](https://github.com/user-attachments/assets/61cafd1d-6293-45f0-81de-f81908d17530)
   ![Image](https://github.com/user-attachments/assets/13b99785-dcc3-4cf5-9b25-7d6af3d65324)
   ![Image](https://github.com/user-attachments/assets/7c4f3ebb-6785-4e01-a125-c5d1a0e2501c)

3. **Start the Local Server**:

* In LM Studio, select your downloaded model
* Click on "Local Server" in the left sidebar
* Click "Start Server"
* The server will run by default at [http://127.0.0.1:1234/v1](http://127.0.0.1:1234/v1)

   
   ![Image](https://github.com/user-attachments/assets/8aefe6cd-2609-4b4a-a520-fd15ece3847f)

4. **Configure the AI Prompt Optimizer**:

* In the AI Prompt Optimizer application, select "LM Studio (local)" as the LLM backend
* The application will automatically connect to the local server


   ![Image](https://github.com/user-attachments/assets/1e222b36-3f1f-4bd3-ada0-79d7fd0c0d4b)
   ![Image](https://github.com/user-attachments/assets/ca736c75-68e2-46d5-a7e1-4c42d259db9e)
   ![Image](https://github.com/user-attachments/assets/928d1243-959a-4d8c-888c-57142cdc4d8b)

## Using the Google Gemini API

To use the Google Gemini API:

1. **Obtain an API Key**:

* Visit [Google AI Studio](https://aistudio.google.com/)
* Create an account if you don’t have one
* Generate an API key

2. **Configure the Application**:

* In the AI Prompt Optimizer, select "Google Gemini Flash 2.0 (API)" as the LLM backend
* Enter your API key in the designated field
* The key will be saved for future sessions


   ![Image](https://github.com/user-attachments/assets/888788bb-61c8-4ef2-a134-c652dd297daa)
   ![Image](https://github.com/user-attachments/assets/182e76c8-734f-4695-9217-a783e0fbd0e9)

## User Guide

### Basic Prompt Optimization

1. Select your target image model (SDXL, Stable Diffusion 1.5, etc.)
2. Choose your preferred LLM backend
3. Enter a description of the desired image in the text field
4. Adjust the sliders for detail level, prompt length, and visual style as needed
5. Click "Optimize Prompt"
6. View the optimized prompt and its evaluation score
7. Use the "Copy to Clipboard" button to copy the result

### Batch Processing

1. Prepare a TXT file (one description per line) or a CSV file
2. Go to the "Batch Processing" tab
3. Upload your file
4. Click "Process Batch"
5. View the results table
6. Export the results in your preferred format

### History and Export

* Access your prompt history in the "History" tab to review past optimizations
* Use the export options to save your prompts in TXT, JSON, or CSV format

### Save and Export

* Use export options to save your prompts in TXT, JSON, or CSV formats
* Access your prompt history in the "History" tab
* Rate and provide feedback on prompts to improve future generations

## Troubleshooting

### Common Issues

* **LM Studio Connection Error**: Ensure the LM Studio server is running and accessible at [http://127.0.0.1:1234/v1](http://127.0.0.1:1234/v1)
* **Google Gemini API Error**: Verify your API key is correct and not expired
* **Installation Failure**: Make sure Python 3.8+ is installed and available in your PATH
* **Application Crash**: Check that all dependencies are properly installed

### Getting Help

If you encounter issues not covered here:

* Visit the [GitHub Issues page](https://github.com/votrenomdutilisateur/optimiseur-prompts-ia/issues)
* Submit a new issue with details about your problem
* Contact the maintainer at [k.kurt@outlook.fr](mailto:k.kurt@outlook.fr)

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add an amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Special thanks to the developers of Gradio, which powers my interface
* Recognition to the creators of the image generation models supported by this tool

## Support the Project

If the AI Prompt Optimizer helps in your creative workflow, please consider supporting its development. Your contributions help maintain the project and add new features.
If you wish, and especially if you can, support this project and my future ongoing projects!

Visit my Patreon link: https://www.patreon.com/preview/campaign?u=172098706&fan_landing=true&view_as=public


