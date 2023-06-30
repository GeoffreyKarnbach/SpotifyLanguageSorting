import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

BASE_URL = "https://spotify-lyric-api.herokuapp.com/?trackid="

def get_url_for_uri(uri):
    return BASE_URL + uri

def get_lyrics_for_uri(uri):
    url = get_url_for_uri(uri)
    response = requests.get(url)
    if response.json()["error"] == False:
        return ". ".join([item["words"] for item in response.json()["lines"]])
    else:
        return None

def get_title_from_uri(uri):
    with open(".env", "r") as f:
        os.environ["SPOTIPY_CLIENT_ID"]=f.readline().strip().split("=")[-1]
        os.environ["SPOTIPY_CLIENT_SECRET"]=f.readline().strip().split("=")[-1]
        os.environ["SPOTIPY_REDIRECT_URI"]=f.readline().strip().split("=")[-1]

    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    info = sp.track(uri)
    if info is None:
        return None
    
    return info["name"]

if __name__ == "__main__":
    print(get_lyrics_for_uri("4cOdK2wGLETKBW3PvgPWqT"))
    print(get_title_from_uri("4cOdK2wGLETKBW3PvgPWqT"))
