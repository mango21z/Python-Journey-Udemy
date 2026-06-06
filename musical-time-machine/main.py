import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth


spotify_client = os.getenv("SPOTIFY_CLIENT")
spotify_secret = os.getenv("SPOTIFY_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
# user_id = os.getenv("SPOTIFY_USERID")
spotify_endpoint = "https://api.spotify.com/v1/me/playlists"

date = str(input("which year do you want to travel to? YYYY-MM-DD\n"))

url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


song_name = soup.find_all(name="h3", class_="chart-entry__title")
artist_name = soup.find_all("span", class_="chart-entry__artist")

song_list = [song.getText() for song in song_name]
artist_list = [artist.getText() for artist in artist_name]
print(song_list)
print(artist_list)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client,
                                               client_secret=spotify_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-private",
                                               cache_path="token.txt",
                                               username="mango"
                                               ))

user_id = sp.current_user()["id"]




song_uris = []
year = date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is not on spotify")

playlist = sp.current_user_playlist_create(name=f"{date}", public=False, collaborative=False, description="play this list immediately after created")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
