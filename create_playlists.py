# Fetch all songs from favorite playlist from spotify

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def create_playlists():
    with open(".env", "r") as f:
        os.environ["SPOTIPY_CLIENT_ID"]=f.readline().strip().split("=")[-1]
        os.environ["SPOTIPY_CLIENT_SECRET"]=f.readline().strip().split("=")[-1]
        os.environ["SPOTIPY_REDIRECT_URI"]=f.readline().strip().split("=")[-1]

    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    base_name_track = "spotify:track:"

    with open("uris_languages.txt", "r") as f:
        uris_languages = f.read().split("\n")
    
    uris_languages = [uri.split(" ") for uri in uris_languages]
    
    uris_german = [base_name_track + uri[0] for uri in uris_languages if uri[1] == "German"]
    uris_english = [base_name_track + uri[0] for uri in uris_languages if uri[1] == "English"]
    uris_french = [base_name_track + uri[0] for uri in uris_languages if uri[1] == "French"]
    uris_undefined = [base_name_track + uri[0] for uri in uris_languages if uri[1] == "undefined"]

    uris_english.extend(uris_undefined)

    sp.playlist_replace_items

    print("Adding german songs to playlists")
    sp.playlist_replace_items("spotify:playlist:62EBcsyhwEXJv9B49qczBG", [])
    for group in [uris_german[x:x+100] for x in range(0, len(uris_german), 100)]:
        sp.playlist_add_items("spotify:playlist:62EBcsyhwEXJv9B49qczBG", group)
    
    print("Adding english songs to playlists")
    sp.playlist_replace_items("spotify:playlist:06DpDaDzIqr31XUZVwqK2s", [])
    for group in [uris_english[x:x+100] for x in range(0, len(uris_english), 100)]:
        sp.playlist_add_items("spotify:playlist:06DpDaDzIqr31XUZVwqK2s", group)

    print("Adding french songs to playlists")
    sp.playlist_replace_items("spotify:playlist:1dT7LiJGMh7FtpSS66pDUI", [])
    for group in [uris_french[x:x+100] for x in range(0, len(uris_french), 100)]:
        sp.playlist_add_items("spotify:playlist:1dT7LiJGMh7FtpSS66pDUI", group)

    print("Done")

if __name__ == "__main__":
    create_playlists()