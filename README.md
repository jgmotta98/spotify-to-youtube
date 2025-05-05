<h1 align="center">
  <b>Spotify to Youtube</b>
  <br>
</h1>

This project allows users to seamlessly transfer their Spotify playlists to YouTube. By leveraging Spotify's API and YouTube's API, users can automate the process of creating YouTube playlists based on their Spotify library.

## APIs Configuration

Before running the code, ensure that you configure and adjust the necessary APIs and files. For detailed instructions on **API configuration**, please refer to the [APIs documentation](./APIs.md).

> The YouTube API has a daily limit of 10,000 units, with each API request consuming 100 units, limiting the number of calls per day using a free tier.

## Installation

After configuring the APIs, clone the repository:
```sh
git clone https://github.com/jgmotta98/spotify-to-youtube.git
cd spotify-to-youtube
```

Install dependencies:
```sh
pip install -r requirements.txt
```

Create an `.env` file with the proper tokens:
```sh
SPOTIFY_CLIENT_ID='your_key'
SPOTIFY_CLIENT_SECRET='your_key'
```

Change the Spotify playlist link on the `main.py` file:
```sh
PLAYLIST_URL = 'https://open.spotify.com/playlist/...'
```

Run the `main.py` file:
```sh
python main.py
```

## License

[MIT](./LICENSE) © Spotify to Youtube