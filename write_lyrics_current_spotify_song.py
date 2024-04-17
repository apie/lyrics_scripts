#!/usr/bin/env python3
from pathlib import Path
from rich import print
from print_spotify_lyrics import get_current_song_info_and_lyrics

if __name__ == "__main__":
    info = get_current_song_info_and_lyrics()
    artist, album, title, lyrics = info.values()
    print(f"Song: '{title}' by '{artist}'.")
    if not lyrics:
        raise Exception('Lyrics not found!')
    pt = (Path.cwd() / 'lyrics' / artist / album / title).with_suffix('.txt')
    pt.parent.mkdir(parents=True, exist_ok=True)
    if pt.exists():
        print('Lyrics already downloaded!')
    else:
        pt.write_text(lyrics)
        print('Done saving lyrics.')

