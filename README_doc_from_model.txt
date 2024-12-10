D'accord, je vais réessayer. Voici un exemple de code Python qui utilise l'API Google Docs pour générer un modèle de plan de travail :

Python

from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Si vous modifiez ces champs d'application, supprimez le fichier token.json.
SCOPES = ['https://www.googleapis.com/auth/documents']

# ID du document modèle de plan de travail
DOCUMENT_ID = 'VOTRE_DOCUMENT_ID'

def main():
    """Montre comment utiliser l'API Google Docs pour créer un document.
    """
    creds = None
    # Le fichier token.json stocke les jetons d'accès et d'actualisation de l'utilisateur, et est
    # créé automatiquement lorsque le flux d'autorisation est terminé pour la première
    # fois.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Si aucune information d'identification valide n'est disponible, laissez l'utilisateur se connecter.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Enregistrez les informations d'identification pour la prochaine exécution
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('docs', 'v1', credentials=creds)

    # Crée une copie du document modèle
    body = {
        'name': 'Mon plan de travail'
    }
    doc = service.documents().copy(documentId=DOCUMENT_ID, body=body).execute()
    doc_id = doc.get('documentId')

    print('Plan de travail créé avec ID : {0}'.format(doc_id))

if __name__ == '__main__':
    main()
Explication du code :

Authentification : Le code commence par s'authentifier auprès de l'API Google Docs en utilisant les informations d'identification de votre projet Google Cloud.
Copie du modèle : Ensuite, il utilise la méthode documents().copy() pour créer une copie du document modèle spécifié par DOCUMENT_ID. Vous devez remplacer VOTRE_DOCUMENT_ID par l'ID de votre document modèle.
Affichage de l'ID : Enfin, le code affiche l'ID du nouveau document créé.
Pour utiliser ce code :

Installez la bibliothèque Google API Client pour Python :
Bash

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
Activez l'API Google Docs dans votre projet Google Cloud :
Allez sur la console Google Cloud.
Créez ou sélectionnez un projet.
Activez l'API Google Docs.
Créez un document modèle de plan de travail dans Google Docs.
Remplacez VOTRE_DOCUMENT_ID par l'ID de votre document modèle.
Exécutez le code Python.
Ce code créera une copie de votre modèle de plan de travail. Vous pouvez ensuite modifier ce nouveau document pour l'adapter à vos besoins.

Améliorations possibles :

Modifier le contenu du plan de travail dynamiquement : Vous pouvez utiliser la méthode documents().batchUpdate() pour modifier le contenu du plan de travail, par exemple pour ajouter des tâches, modifier des dates, etc.
Ajouter des fonctionnalités supplémentaires : Vous pouvez ajouter des fonctionnalités comme la possibilité de choisir un modèle parmi plusieurs, de personnaliser le nom du nouveau document, etc.
N'hésitez pas à me poser des questions si vous avez besoin d'aide pour comprendre ou modifier ce code.