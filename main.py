from fetch_all_from_favorite import fetch_all_liked_songs
from get_info_for_uri import get_lyrics_for_uri, get_title_from_uri
from decision_tree import evaluate_language_for_text_module, evaluate_language_for_text_own
from create_playlists import create_playlists

import os

def main():

    lang_match = {"en": "English", "de": "German", "fr": "French"}

    print("Fetching URIs of all songs from favorite playlist from spotify")

    uris = []
    if not os.path.exists("uris.txt"):
        uris = fetch_all_liked_songs()
    else:
        with open("uris.txt", "r") as f:
            uris = f.read().split("\n")

    print("Fetching lyrics for all songs")
    for idx,uri in enumerate(uris):
        print("Fetching lyrics for song " + str(idx+1) + " of " + str(len(uris)))

        try:      
            lyrics = get_lyrics_for_uri(uri)
            title = get_title_from_uri(uri)

            language_title = evaluate_language_for_text_module(title)
            
            result = None
            if lyrics is not None:
                language = evaluate_language_for_text_module(lyrics)
                result = language

                if language_title != language:
                    print("Language for title and lyrics do not match for song " + str(idx+1) + " of " + str(len(uris)))
                    print("Title: " + title)
                    print("Title language: " + language_title)
                    print("Lyrics language: " + language + "\n")

                if language == "undefined":
                    result = language_title
                
            else:
                result = language_title
            
            result = lang_match[result] if result in lang_match else result
            
            with open("uris_languages.txt", "a") as f:
                f.write(str(uri).split(":")[-1] + " " + result)
                if idx != len(uris) - 1:
                    f.write("\n")
        except:
            print("Error occured for song " + str(idx+1) + " of " + str(len(uris)))
            with open("uris_languages.txt", "a") as f:
                f.write(str(uri).split(":")[-1] + " undefined")

                if idx != len(uris) - 1:
                    f.write("\n")

    print("Creating playlists")
    create_playlists()

    print("Done")

if __name__ == "__main__":
    main()