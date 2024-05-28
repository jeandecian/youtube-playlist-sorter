from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_authenticated_service(
    api_service_name, api_version, client_secrets_file, scopes
):
    return build(
        api_service_name,
        api_version,
        credentials=InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes
        ).run_local_server(port=0),
    )


get_authenticated_service(API_SERVICE_NAME, API_VERSION, CLIENT_SECRETS_FILE, SCOPES)
