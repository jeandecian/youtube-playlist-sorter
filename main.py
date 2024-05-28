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


def get_all_playlists(youtube):
    playlists = []
    next_page_token = None

    while True:
        response = (
            youtube.playlists()
            .list(
                part="snippet,contentDetails",
                mine=True,
                maxResults=50,
                pageToken=next_page_token,
            )
            .execute()
        )

        for item in response.get("items"):
            playlists.append(
                {
                    "id": item.get("id"),
                    "title": item.get("snippet").get("title"),
                    "itemCount": item.get("contentDetails").get("itemCount"),
                }
            )

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return playlists


youtube = get_authenticated_service(
    API_SERVICE_NAME, API_VERSION, CLIENT_SECRETS_FILE, SCOPES
)
playlists = get_all_playlists(youtube)

for playlist in playlists:
    print(
        f"ID: {playlist.get("id")}, Title: {playlist.get("title")}, Items: {playlist.get("itemCount")}"
    )
