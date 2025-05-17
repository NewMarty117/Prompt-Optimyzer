@echo off
echo Lancement de l'Optimiseur de Prompts IA...

REM Vérifier si l'environnement virtuel existe
IF NOT EXIST .\venv\Scripts\activate.bat (
    echo Environnement virtuel non trouvé. Veuillez exécuter install.bat d'abord.
    pause
    exit /b 1
)

REM Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call .\venv\Scripts\activate.bat

REM Lancer l'application Python en arrière-plan
echo Lancement de l'application Python (serveur)...
REM Le "start" permet de lancer python app.py et de continuer l'exécution du script batch
REM On donne un titre à la fenêtre du serveur pour la reconnaître facilement
start "Serveur IA Prompts" python app.py

REM Attendre quelques secondes que le serveur démarre
echo Attente du démarrage du serveur (5 secondes)...
REM /t 5 pour 5 secondes. Ajustez si votre app met plus de temps à démarrer.
REM /nobreak pour que l'attente ne soit pas interrompue par une touche.
REM >nul pour masquer le compte à rebours du timeout.
timeout /t 5 /nobreak >nul

REM Ouvrir le navigateur sur l'URL spécifiée
echo Ouverture de l'application dans le navigateur sur http://127.0.0.1:7860/
start http://127.0.0.1:7860/

echo Le script de lancement a terminé. Le serveur IA devrait tourner dans sa propre fenêtre.
echo Pour arrêter le serveur, fermez la fenêtre nommée "Serveur IA Prompts".
REM Pas besoin de pause ici, car le script a fait son travail.
REM Si vous voulez quand même garder cette fenêtre ouverte pour lire les messages :
REM pause