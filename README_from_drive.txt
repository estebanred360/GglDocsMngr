Étape 1 : Télécharger le Fichier .docx sur Google Drive
Télécharger le Fichier :

Ouvrez Google Drive.
Cliquez sur le bouton Nouveau et sélectionnez Téléverser un fichier.
Sélectionnez votre fichier .docx et téléchargez-le.
Obtenir l'ID du Fichier :

Une fois le fichier téléchargé, cliquez dessus pour l'ouvrir.
Regardez l'URL dans la barre d'adresse de votre navigateur. Elle ressemblera à ceci :

https://drive.google.com/file/d/FILE_ID/view?usp=sharing
L'ID du fichier est la partie de l'URL entre /d/ et /view. Par exemple, si l'URL est https://drive.google.com/file/d/1abcdefghijklmnopqrstuvwxyz/view?usp=sharing, l'ID du fichier est 1abcdefghijklmnopqrstuvwxyz.
Étape 2 : Utiliser l'ID du Fichier dans le Script
Voici le script Google Apps Script mis à jour pour lire un fichier .docx stocké sur Google Drive et générer un document Google Sheets structuré :

Étape 3 : Exécuter le Script
Ouvrez Google Sheets et créez un nouveau document ou ouvrez un document existant.
Cliquez sur Extensions > Apps Script.
Supprimez tout le code par défaut dans l'éditeur de script.
Copiez et collez le script ci-dessus dans l'éditeur de script.
Remplacez 'ID_DE_VOTRE_FICHIER_DOCX' par l'ID de votre fichier .docx.
Cliquez sur l'icône de la disquette pour enregistrer votre script.
Cliquez sur l'icône de lecture (triangle) pour exécuter le script.
La première fois que vous exécutez le script, vous devrez autoriser les permissions nécessaires. Suivez les instructions à l'écran pour accorder les permissions.
Conclusion
Ce script lit un fichier .docx contenant les statuts d'une SAS stocké sur Google Drive et génère un document Google Sheets structuré avec des colonnes pour les chapitres, sous-chapitres et articles, ainsi que des onglets séparés pour chaque annexe. Vous pouvez personnaliser le script en fonction de la structure spécifique de votre fichier .docx.