import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def spotify_song_names(client_id: str, client_secret: str, playlist_url: str) -> tuple[str, list[str]]:
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    playlist_data = sp.playlist(playlist_id)
    playlist_name = playlist_data['name']

    results = sp.playlist_tracks(playlist_id)
    songs = results['items']
    
    track_info = [
        (track['track']['name'], track['track']['artists'][0]['name'])
        for track in songs
    ]

    return (playlist_name, track_info)
