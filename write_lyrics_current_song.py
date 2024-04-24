#!/usr/bin/env python3
from pathlib import Path
from rich import print
from print_currently_playing_metadata import get_current_song_info
from print_currently_playing_lyrics import get_current_song_info_and_lyrics

if __name__ == "__main__":
    info = get_current_song_info()
    artist, album, title = info.values()
    print(f"Song: '{title}' by '{artist}'.")
    pt = (Path.cwd() / 'lyrics' / artist / album / title).with_suffix('.txt')
    pt.parent.mkdir(parents=True, exist_ok=True)
    if pt.exists():
        print('Lyrics already downloaded!')
    else:
        lyrics = get_current_song_info_and_lyrics()['lyrics']
        if not lyrics:
            raise Exception('Lyrics not found!')
        pt.write_text(lyrics)
        print('Done saving lyrics.')

