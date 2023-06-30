# Fetch all songs from favorite playlist from spotify

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def fetch_all_liked_songs():
    with open(".env", "r") as f:
        os.environ["SPOTIPY_CLIENT_ID"]=f.readline().strip().split("=")[-1]
        os.environ["SPOTIPY_CLIENT_SECRET"]=f.readline().strip().split("=")[-1]
        os.environ["SPOTIPY_REDIRECT_URI"]=f.readline().strip().split("=")[-1]

    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_saved_tracks()

    if results is None:
        print("No songs found")
        return
    
    songs = results['items']

    while results['next']:
        results = sp.next(results)
        songs.extend(results['items'])

    uris = []

    for idx, item in enumerate(songs):
        track = item['track']
        uris.append(track["uri"])

    with open("uris.txt", "w") as f:
        for idx,uri in enumerate(uris):
            f.write(str(uri).split(":")[-1])
            if idx != len(uris)-1:
                f.write("\n")
    
    return uris

if __name__ == "__main__":
    fetch_all_liked_songs()