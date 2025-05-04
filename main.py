from src.spotify_manager import spotify_song_names
from src.youtube_manager import create_youtube_playlist
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
PLAYLIST_URL = 'https://open.spotify.com/playlist/...'


def main() -> None:
    playlist_name, spotify_names = spotify_song_names(client_id, client_secret, PLAYLIST_URL)
    create_youtube_playlist(playlist_name, spotify_names)


if __name__ == "__main__":
    main()