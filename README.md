# Optimiseur de Prompts IA

L'Optimiseur de Prompts IA est une application puissante conçue pour améliorer et optimiser les prompts textuels pour les modèles de génération d'images IA. Cet outil aide les utilisateurs à créer des prompts plus efficaces qui produisent de meilleurs résultats avec des modèles comme SDXL, Stable Diffusion 1.5, Flux 1.0 dev et HiDream.

![Image](https://github.com/user-attachments/assets/fce20773-b228-446f-8743-7f1398aca358)

## Fonctionnalités

- **Saisie en langage naturel** : Décrivez votre scène en termes simples dans n'importe quelle langue
- **Traduction automatique** : Saisissez dans n'importe quelle langue, obtenez des prompts optimisés en anglais (requis par les modèles d'image)
- **Support de plusieurs modèles d'image** : Optimisation pour SDXL, Stable Diffusion 1.5, Flux 1.0 dev ou HiDream
- **Options flexibles de backend LLM** :
  - Traitement local avec LM Studio
  - Traitement cloud avec l'API Google Gemini Flash 2.0
- **Contrôles avancés** :
  - Ajustement du niveau de détail
  - Contrôle de la longueur du prompt
  - Curseur de style visuel (brut à professionnel)
- **Raisonnement en cascade** : Optimisation logique spécifique à chaque modèle d'image
- **Traitement par lots** : Importez des fichiers TXT ou CSV contenant plusieurs descriptions
- **Évaluation automatique des prompts** : Système de notation de qualité pour les prompts générés
- **Système de feedback utilisateur** : Notez et commentez les prompts générés
- **Interface multilingue** : Disponible en français et en anglais
- **Options d'exportation faciles** : Enregistrez les résultats en TXT, JSON ou CSV

## Guide d'installation

### Prérequis

- Windows 10 64 bits ou plus récent
- Python 3.8 ou plus récent
- Connexion Internet (pour la configuration initiale et lors de l'utilisation de l'API Google Gemini)
- [LM Studio](https://lmstudio.ai/) (optionnel, pour le traitement LLM local)

### Installation standard

1. **Téléchargez l'application** :
   - Téléchargez la dernière version depuis ma page
   - Extrayez le fichier ZIP à l'emplacement de votre choix

2. **Exécutez le script d'installation** :
   - Ouvrez le dossier extrait
   - Double-cliquez sur `install.bat`
   - Attendez que l'installation se termine (cela créera un environnement virtuel et installera toutes les dépendances)
   
   ![Image](https://github.com/user-attachments/assets/5ed99175-8e98-4817-ae31-84be9990a8bc)

3. **Lancez l'application** :
   - Une fois l'installation terminée, double-cliquez sur `launcher.bat`
   - L'application s'ouvrira dans votre navigateur web par défaut
   
   ![Image](https://github.com/user-attachments/assets/00400ad8-aeed-4983-bb19-db81605bbd0a)

### Installation manuelle (utilisateurs avancés)

Si vous préférez installer manuellement :

1. Créez un environnement virtuel :
   ```
   python -m venv venv
   ```

2. Activez l'environnement virtuel :
   ```
   venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

4. Lancez l'application :
   ```
   python app.py
   ```

## Configuration de LM Studio pour le traitement local

Pour le traitement LLM local sans dépendre d'API externes, vous pouvez utiliser LM Studio :

1. **Téléchargez et installez LM Studio** :
   - Téléchargez depuis [lmstudio.ai](https://lmstudio.ai/)
   - Suivez les instructions d'installation
   
   ![Image](https://github.com/user-attachments/assets/c2143d38-6e1d-476a-9a7f-fcf4a546a202)

2. **Téléchargez un modèle compatible** :
   - Ouvrez LM Studio
   - Allez dans l'onglet "Models"
   - Téléchargez un modèle adapté à la génération de texte (recommandé : Mistral 7B, Llama 2 ou similaire)
   
   ![Image](https://github.com/user-attachments/assets/61cafd1d-6293-45f0-81de-f81908d17530)
   ![Image](https://github.com/user-attachments/assets/13b99785-dcc3-4cf5-9b25-7d6af3d65324)
   ![Image](https://github.com/user-attachments/assets/7c4f3ebb-6785-4e01-a125-c5d1a0e2501c)

3. **Démarrez le serveur local** :
   - Dans LM Studio, sélectionnez votre modèle téléchargé
   - Cliquez sur "Local Server" dans la barre latérale gauche
   - Cliquez sur "Start Server"
   - Le serveur fonctionnera par défaut sur http://127.0.0.1:1234/v1
   
   ![Image](https://github.com/user-attachments/assets/8aefe6cd-2609-4b4a-a520-fd15ece3847f)

4. **Configurez l'Optimiseur de Prompts IA** :
   - Dans l'application Optimiseur de Prompts IA, sélectionnez "LM Studio (local)" comme backend LLM
   - L'application se connectera automatiquement au serveur local

   ![Image](https://github.com/user-attachments/assets/1e222b36-3f1f-4bd3-ada0-79d7fd0c0d4b)
   ![Image](https://github.com/user-attachments/assets/ca736c75-68e2-46d5-a7e1-4c42d259db9e)
   ![Image](https://github.com/user-attachments/assets/928d1243-959a-4d8c-888c-57142cdc4d8b)

## Utilisation de l'API Google Gemini

Pour utiliser l'API Google Gemini :

1. **Obtenez une clé API** :
   - Visitez [Google AI Studio](https://aistudio.google.com/)
   - Créez un compte si vous n'en avez pas
   - Générez une clé API

2. **Configurez l'application** :
   - Dans l'Optimiseur de Prompts IA, sélectionnez "Google Gemini Flash 2.0 (API)" comme backend LLM
   - Entrez votre clé API dans le champ prévu
   - La clé sera sauvegardée pour les sessions futures

   ![Image](https://github.com/user-attachments/assets/888788bb-61c8-4ef2-a134-c652dd297daa)
   ![Image](https://github.com/user-attachments/assets/182e76c8-734f-4695-9217-a783e0fbd0e9)

## Guide d'utilisation

### Optimisation de base des prompts

1. Sélectionnez votre modèle d'image cible (SDXL, Stable Diffusion 1.5, etc.)
2. Choisissez votre backend LLM préféré
3. Entrez une description de l'image souhaitée dans le champ de texte
4. Ajustez les curseurs pour le niveau de détail, la longueur du prompt et le style visuel selon vos besoins
5. Cliquez sur "Optimiser le prompt"
6. Visualisez le prompt optimisé et son score d'évaluation
7. Utilisez le bouton "Copier dans le presse-papiers" pour copier le résultat

### Traitement par lots

1. Préparez un fichier TXT (une description par ligne) ou un fichier CSV
2. Allez dans l'onglet "Traitement par lots"
3. Téléchargez votre fichier
4. Cliquez sur "Traiter le lot"
5. Visualisez le tableau des résultats
6. Exportez les résultats dans le format de votre choix


### Historique et exportation

- Accédez à l'historique de vos prompts dans l'onglet "Historique" pour revoir les optimisations passées
- Utilisez les options d'exportation pour sauvegarder vos prompts en format TXT, JSON ou CSV


### Sauvegarde et exportation

- Utilisez les options d'exportation pour sauvegarder vos prompts en format TXT, JSON ou CSV
- Accédez à l'historique de vos prompts dans l'onglet "Historique"
- Notez et fournissez des commentaires sur les prompts pour améliorer les générations futures

## Dépannage

### Problèmes courants

- **Erreur de connexion LM Studio** : Assurez-vous que le serveur LM Studio est en cours d'exécution et accessible à l'adresse http://127.0.0.1:1234/v1
- **Erreur d'API Google Gemini** : Vérifiez que votre clé API est correcte et n'a pas expiré
- **Échec de l'installation** : Assurez-vous que Python 3.8+ est installé et accessible dans votre PATH
- **Plantage de l'application** : Vérifiez que toutes les dépendances sont correctement installées

### Obtenir de l'aide

Si vous rencontrez des problèmes non couverts ici :

- Consultez la page [GitHub Issues](https://github.com/votrenomdutilisateur/optimiseur-prompts-ia/issues)
- Soumettez un nouveau problème avec des détails sur votre problème
- Contactez le mainteneur à [k.kurt@outlook.fr](mailto:k.kurt@outlook.fr)

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

1. Forkez le dépôt
2. Créez votre branche de fonctionnalité (`git checkout -b fonctionnalite/fonctionnalite-incroyable`)
3. Committez vos modifications (`git commit -m 'Ajout d'une fonctionnalité incroyable'`)
4. Poussez vers la branche (`git push origin fonctionnalite/fonctionnalite-incroyable`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- Remerciements spéciaux aux développeurs de Gradio, qui alimente mon interface
- Reconnaissance aux créateurs des modèles de génération d'images que cet outil prend en charge

## Soutenir le Projet

Si l'Optimiseur de Prompts IA vous est utile dans votre flux de travail créatif, merci d'envisager de soutenir son développement. Vos contributions aident à maintenir le projet, et à ajouter de nouvelles fonctionnalités.
Si vous le souhaitez, et surtout si vous le pouvez, soutenez le projet ainsi que mes futurs projets en cours !

Visitez mon lien Patreon: https://www.patreon.com/preview/campaign?u=172098706&fan_landing=true&view_as=public


