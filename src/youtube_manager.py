import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube"]


def get_authenticated_service():
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


def create_playlist(youtube, title, description="Created with Python"):
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
    print(f"Created playlist: {response['snippet']['title']}")
    return response["id"]


def search_video(youtube, query):
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


def add_video_to_playlist(youtube, playlist_id, video_id):
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
    print(f"Added video {video_id} to playlist")


from googleapiclient.discovery import build, Resource


def search_video(query: str, youtube: Resource) -> str | None:
        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=query,
            type="video"
        )
        response = request.execute()
        items = response.get("items", [])
        if items:
            video_id = items[0]["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"
        
        return None


def youtube_video_link(api_key: str, spotify_song_names: list[tuple[str, str]]) -> list[str]:
    youtube = build("youtube", "v3", developerKey=api_key)

    songs_url: list[str] = []
    for song in spotify_song_names:
        url = search_video(f'{song[0]} - {song[1]}', youtube)
        if url:
            songs_url.append(url)
    
    return songs_url


def create_youtube_playlist(playlist_name: str, spotify_song_names: list[tuple[str, str]]) -> None:
    youtube = get_authenticated_service()

    songs = [
        "Radiohead - Creep",
        "Coldplay - Yellow",
        "The Weeknd - Blinding Lights"
    ]

    playlist_id = create_playlist(youtube, "My Spotify Playlist")

    for song in songs:
        video_id = search_video(youtube, song)
        if video_id:
            add_video_to_playlist(youtube, playlist_id, video_id)
        else:
            print(f"Video not found: {song}")
