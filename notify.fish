#!/usr/bin/fish
set DIR (realpath (dirname (status -f)))
notify-send ($DIR/print_currently_playing_metadata.py)
