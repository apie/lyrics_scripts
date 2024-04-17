#!/usr/bin/env python3
import dbus
from rich import print
from dbus import Interface
bus = dbus.SessionBus()
proxy = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
interface = dbus.Interface(proxy, dbus_interface='org.mpris.MediaPlayer2.Player')
#interface.PlayPause()
props_iface = Interface(proxy, dbus_interface='org.freedesktop.DBus.Properties')

def get_metadata():
    return props_iface.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    # OUT: [dbus.String(u'xesam:album'), dbus.String(u'xesam:title'), dbus.String(u'xesam:trackNumber'), dbus.String(u'xesam:artist'), dbus.String(u'xesam:discNumber'), dbus.String(u'mpris:trackid'), dbus.String(u'mpris:length'), dbus.String(u'mpris:artUrl'), dbus.String(u'xesam:autoRating'), dbus.String(u'xesam:contentCreated'), dbus.String(u'xesam:url')]

if __name__ == "__main__":
    info = get_metadata()
    artist, title = info['xesam:artist'][0], info['xesam:title']
    print(f"Song: '{title}' by '{artist}'.")

