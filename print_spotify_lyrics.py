#!/usr/bin/env python3
from print_spotify_metadata import get_metadata
from getMMlyrics import get_mm_lyrics, get_mm_credentials

def get_current_song_info_and_lyrics():
    info = get_metadata()
    artist = str(info['xesam:artist'][0])
    title = str(info['xesam:title'])
    album = str(info['xesam:album'])
    short, full = get_mm_lyrics(creds=get_mm_credentials(verbose=0), artist=artist, title=title, verbose=0)
    return dict(artist=artist, album=album, title=title, lyrics=short['lyrics'])

if __name__ == "__main__":
    print(get_current_song_info_and_lyrics()['lyrics'])

