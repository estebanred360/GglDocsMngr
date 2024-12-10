from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# # # #
# Si vous modifiez ces champs d'application, supprimez le fichier token.json.
SCOPES = ['https://www.googleapis.com/auth/documents']

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

    # Crée un nouveau document
    doc = service.documents().create(body={'title': 'Modèle de plan de travail'}).execute()
    doc_id = doc.get('documentId')

    # Définit le contenu du modèle
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': 'Nom du projet\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': 16,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 16,
                },
                'text': 'Chef de projet\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 16,
                    'endIndex': 31,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 31,
                },
                'text': 'Date de début et date de fin\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 31,
                    'endIndex': 59,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 59,
                },
                'text': 'Objectifs du projet\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 59,
                    'endIndex': 80,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 80,
                },
                'text': 'Livrables\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 80,
                    'endIndex': 90,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 90,
                },
                'text': 'Tâches\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 90,
                    'endIndex': 97,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 97,
                },
                'text': 'Budget\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 97,
                    'endIndex': 104,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 104,
                },
                'text': 'Risques\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 104,
                    'endIndex': 112,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
        {
            'insertText': {
                'location': {
                    'index': 112,
                },
                'text': 'Communication\n',
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 112,
                    'endIndex': 126,
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                },
                'fields': 'namedStyleType',
            }
        },
    ]

    # Applique les modifications
    result = service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()

    print('Modèle de plan de travail créé avec ID : {0}'.format(doc_id))

if __name__ == '__main__':
    main()