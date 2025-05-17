# Optimiseur de Prompts IA

L'Optimiseur de Prompts IA est une application puissante conçue pour améliorer et optimiser les prompts textuels pour les modèles de génération d'images IA. Cet outil aide les utilisateurs à créer des prompts plus efficaces qui produisent de meilleurs résultats avec des modèles comme SDXL, Stable Diffusion 1.5, Flux 1.0 dev et HiDream.

![Interface](https://private-user-images.githubusercontent.com/188101812/444799975-63c82d50-d7ba-485e-8647-5e24d92d4e24.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MTE2MTksIm5iZiI6MTc0NzUxMTMxOSwicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTc1LTYzYzgyZDUwLWQ3YmEtNDg1ZS04NjQ3LTVlMjRkOTJkNGUyNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxOTQ4MzlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kOTg3OTU1MGUyZTI2NWQ4MTJlODRkOWNiYWY1ODM1OGQzOWYyYTUzYjIzMmVjNWIyOTI2MzZjYTgzNDFlYjY3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.9lOrWmZz-H7Ow1QeXBFeIzY5Zq3v1OphtLk9pkHlrHs)

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
   
   ![Install.bath](https://private-user-images.githubusercontent.com/188101812/444799953-8b01939f-a042-4b7b-82e7-f9b86d000889.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDQwNzAsIm5iZiI6MTc0NzUwMzc3MCwicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTUzLThiMDE5MzlmLWEwNDItNGI3Yi04MmU3LWY5Yjg2ZDAwMDg4OS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxNzQyNTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zYmNhNzE5NDNjMWRjMDczZDNiNGUyNzRmNTJiZWFkM2JkOTExNmMxOWVhYmQxMTY1OTRjNTc5OGNjMzI4MzVkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.XUeHHswV1Sl7IyomEOCiOae04FSWKy1IYNlASgE_vLE)

3. **Lancez l'application** :
   - Une fois l'installation terminée, double-cliquez sur `launcher.bat`
   - L'application s'ouvrira dans votre navigateur web par défaut
   
   ![Install.bath](https://private-user-images.githubusercontent.com/188101812/444799967-80a99b60-30cb-4ba4-9b6d-c1596e825d56.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDUzMTIsIm5iZiI6MTc0NzUwNTAxMiwicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTY3LTgwYTk5YjYwLTMwY2ItNGJhNC05YjZkLWMxNTk2ZTgyNWQ1Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODAzMzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZjMxODAxMWY4MjkxM2I0NjMzNzM3MjhmMzMyZDZiYzM5OWU0YTYyMjk4MjYwMWQ5ZmY3ZmQxMWUyYjhlMThkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.0ZiM-QknjqCj5EqUPOi2EEQ9iPeXcCzDbRvhTzMrsuI)

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
   
   ![LmStudio](https://private-user-images.githubusercontent.com/188101812/444799973-8b95040f-8b87-4d76-b48f-cf10b00fb274.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDUzMTIsIm5iZiI6MTc0NzUwNTAxMiwicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTczLThiOTUwNDBmLThiODctNGQ3Ni1iNDhmLWNmMTBiMDBmYjI3NC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODAzMzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZGNhMDRmOTNkZWNlNWFkNjUwMDZiMDhkOTAzODgwYzVjNzA3OWNlNDhiNGI0Yjc0NTNhNjA4MGQ5MjBmMGUwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.CXBXstiDszCjCCtiH6k5sXP4Tv8tt8Rs6PSQ2IPFWOU)

2. **Téléchargez un modèle compatible** :
   - Ouvrez LM Studio
   - Allez dans l'onglet "Models"
   - Téléchargez un modèle adapté à la génération de texte (recommandé : Mistral 7B, Llama 2 ou similaire)
   
   ![Téléchargement](https://private-user-images.githubusercontent.com/188101812/444799954-0b83295e-0615-4ece-bb93-34c191006a82.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDUzMTIsIm5iZiI6MTc0NzUwNTAxMiwicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTU0LTBiODMyOTVlLTA2MTUtNGVjZS1iYjkzLTM0YzE5MTAwNmE4Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODAzMzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMjkxYzYxNTVhOTNkZTU2ZWIzYWU5NTY2OWY1NmM5NDFmNDE2OTA5NWRiOTk3NjBlMDE3ODY4M2I1OTA4ZDRmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.DnROIXNpf1p32C3Ddjh-ON1LTJOt1tAF7Y48RCQ_9Yw)
   ![Configuration de LM Studio](https://private-user-images.githubusercontent.com/188101812/444799969-9afefcce-b9d6-44cc-b809-4052ae399e17.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDU2MjMsIm5iZiI6MTc0NzUwNTMyMywicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTY5LTlhZmVmY2NlLWI5ZDYtNDRjYy1iODA5LTQwNTJhZTM5OWUxNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODA4NDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNzdhNGZiMGY2NjBkYWNmYzUwZmUwNmUxNzJlMWZjZDU4YjdhYmU0NjAzZWRlZDhmNmYyN2VlOTYzNzYwN2RhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.hespqrUOhW23fQtiTyN5E-R3z0lYHUCGAoKJ7LRXELw)
   ![Choix Modèle](https://private-user-images.githubusercontent.com/188101812/444799955-e66bf9c8-44d1-4f03-94c8-0aecf4adcc8b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDU4ODcsIm5iZiI6MTc0NzUwNTU4NywicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTU1LWU2NmJmOWM4LTQ0ZDEtNGYwMy05NGM4LTBhZWNmNGFkY2M4Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODEzMDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xZTM5MjM3MWFhY2I3ODE5ZGNiNjM2Y2JlOThiNjgxZDlmMGUxMzlmZjM5NzNlMTZmNTBhODUyMTJmNzU5ZjViJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.26XQmyNK_SRuiktjDWbEKRbM6Rq17kgotcu8n1-aN7I)

3. **Démarrez le serveur local** :
   - Dans LM Studio, sélectionnez votre modèle téléchargé
   - Cliquez sur "Local Server" dans la barre latérale gauche
   - Cliquez sur "Start Server"
   - Le serveur fonctionnera par défaut sur http://127.0.0.1:1234/v1
   
   ![Démarrage Serveur](https://private-user-images.githubusercontent.com/188101812/444799957-f75f5c55-676d-4aad-87c4-c357b8b160f7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDU4ODcsIm5iZiI6MTc0NzUwNTU4NywicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTU3LWY3NWY1YzU1LTY3NmQtNGFhZC04N2M0LWMzNTdiOGIxNjBmNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODEzMDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MTIwOTBlMzFkNmE5NTlkYzRhNzUxZDhjMDVjMzZkMjJlMDQ2ZjE4NWUzNDAzMGJlNmMwZDUwZDQ4NDlkNmYwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.pWsclwY1S2Nxxj_hfN7EhssrZTYXwD3NG0N3mRWQCSQ)

4. **Configurez l'Optimiseur de Prompts IA** :
   - Dans l'application Optimiseur de Prompts IA, sélectionnez "LM Studio (local)" comme backend LLM
   - L'application se connectera automatiquement au serveur local

   ![Base](https://private-user-images.githubusercontent.com/188101812/444799975-63c82d50-d7ba-485e-8647-5e24d92d4e24.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDU4ODcsIm5iZiI6MTc0NzUwNTU4NywicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTc1LTYzYzgyZDUwLWQ3YmEtNDg1ZS04NjQ3LTVlMjRkOTJkNGUyNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODEzMDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MTVlOTJmZDI1MDU5NTA3ZDM1NDRjMzdlNjQxZDU0MTRjNTgxZTBlYTQ1ZmEyNDMwNGU2YWIwMDBiZTE1ODI0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.M-o2_6CJjhHdPd2ZpkN2Xmr8BGokKt2pKZQ9I-Rqezs)
   ![Choix Modèle](https://private-user-images.githubusercontent.com/188101812/444799970-34be3349-16e2-4383-a799-6e2ed2e92c5b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDU4ODcsIm5iZiI6MTc0NzUwNTU4NywicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTcwLTM0YmUzMzQ5LTE2ZTItNDM4My1hNzk5LTZlMmVkMmU5MmM1Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODEzMDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNzdiOGNjZjIxMjUxZTA2ZjBlZmIwYTdhY2QxZDIxYWViMDk5ZGNkYjBjNmQ3ZmJiM2VmNzcwYmU2ZDNhNTQzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.N8yjfbUk-_Tib5xyNDTp-vDYFzZ3hNjiAAy4nUNx7_E)
   ![Choix API](https://private-user-images.githubusercontent.com/188101812/444799971-7ba85bc1-5d34-4345-a943-521c6e6dad00.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1MDU4ODcsIm5iZiI6MTc0NzUwNTU4NywicGF0aCI6Ii8xODgxMDE4MTIvNDQ0Nzk5OTcxLTdiYTg1YmMxLTVkMzQtNDM0NS1hOTQzLTUyMWM2ZTZkYWQwMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxN1QxODEzMDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMGE3NGJlZjA1Mzc5Y2ZlNDcwNDU4MWRlZDg1NzY3OGZhODE3YzU0YTlkOTUxZTlhN2FlMTgwZWE2MmU2OTRmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.p7IBS2ojXAxpAdDI_-VKGEhanwfMNyPIUikjHssSins)

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

- Merci à tous les contributeurs qui ont aidé au développement
- Remerciements spéciaux aux développeurs de Gradio, qui alimente notre interface
- Reconnaissance aux créateurs des modèles de génération d'images que cet outil prend en charge

## Soutenir le Projet

Si l'Optimiseur de Prompts IA vous est utile dans votre flux de travail créatif, merci d'envisager de soutenir son développement. Vos contributions aident à maintenir le projet, et à ajouter de nouvelles fonctionnalités.
Si vous le souhaitez, et surtout si vous le pouvez, soutenez le projet ainsi que mes futurs projets en cours !

Visitez mon lien Patreon: https://www.patreon.com/preview/campaign?u=172098706&fan_landing=true&view_as=public


