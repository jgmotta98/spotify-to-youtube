import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource

SCOPES = ["https://www.googleapis.com/auth/youtube"]


def get_authenticated_service() -> Resource:
    credentials = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        credentials = flow.run_local_server(port=8080)
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    return build("youtube", "v3", credentials=credentials)


def create_playlist(youtube: Resource, title: str, description="Created with Python") -> str:
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()

    return response["id"]


def search_video(youtube: Resource, query: str) -> str | None:
    request = youtube.search().list(
        part="snippet",
        q=query,
        maxResults=1,
        type="video"
    )
    response = request.execute()
    results = response.get("items", [])
    if results:
        return results[0]["id"]["videoId"]
    
    return None


def add_video_to_playlist(youtube: Resource, playlist_id: str, video_id: str) -> None:
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    request.execute()


def create_youtube_playlist(playlist_name: str, spotify_song_names: list[tuple[str, str]]) -> None:
    youtube = get_authenticated_service()

    playlist_id = create_playlist(youtube, playlist_name)

    for song in spotify_song_names:
        video_id = search_video(youtube, f'{song[0]} - {song[1]}')
        if video_id:
            add_video_to_playlist(youtube, playlist_id, video_id)
        else:
            print(f"Video not found: {song[0]} - {song[1]}")
