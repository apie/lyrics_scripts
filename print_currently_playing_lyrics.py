#!/usr/bin/env python3
from print_currently_playing_metadata import get_current_song_info
from getMMlyrics import get_mm_lyrics, get_mm_credentials

def get_current_song_info_and_lyrics():
    info = get_current_song_info()
    artist, album, title = info['artist'], info['album'], info['title']
    short, full = get_mm_lyrics(creds=get_mm_credentials(verbose=0), artist=artist, title=title, verbose=0)
    return dict(artist=artist, album=album, title=title, lyrics=short['lyrics'])

if __name__ == "__main__":
    print(get_current_song_info_and_lyrics()['lyrics'])

