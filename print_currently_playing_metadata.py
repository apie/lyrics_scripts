#!/usr/bin/env python3
import dbus
from rich import print
from dbus import Interface

def get_players():
    bus = dbus.SessionBus()
    for name in bus.list_names():
        if name.startswith('org.mpris.MediaPlayer2.'):
            proxy = bus.get_object(name, '/org/mpris/MediaPlayer2')
            yield Interface(proxy, dbus_interface='org.freedesktop.DBus.Properties')

def get_active_player():
    for player in get_players():
        if player.Get("org.mpris.MediaPlayer2.Player", "PlaybackStatus") == 'Playing':
            return player  # Return first playing player.
    raise Exception('No playing players found! Start your player first and play a song.')

def get_metadata():
    return get_active_player().Get("org.mpris.MediaPlayer2.Player", "Metadata")
    ''' [
        dbus.String(u'xesam:album'),
        dbus.String(u'xesam:title'),
        dbus.String(u'xesam:trackNumber'),
        dbus.String(u'xesam:artist'),
        dbus.String(u'xesam:discNumber'),
        dbus.String(u'mpris:trackid'),
        dbus.String(u'mpris:length'),
        dbus.String(u'mpris:artUrl'),
        dbus.String(u'xesam:autoRating'),
        dbus.String(u'xesam:contentCreated'),
        dbus.String(u'xesam:url')
    ]
    '''

def get_current_song_info():
    info = get_metadata()
    artist_info = info['xesam:artist']
    if isinstance(artist_info, list):
        artist_info = artist_info[0]
    artist = str(artist_info)
    title = str(info['xesam:title'])
    album = str(info['xesam:album'])
    return dict(artist=artist, album=album, title=title)

if __name__ == "__main__":
    info = get_current_song_info()
    artist, title = info['artist'], info['title']
    print(f"Song: '{title}' by '{artist}'.")

