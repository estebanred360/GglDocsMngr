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