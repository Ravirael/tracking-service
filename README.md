# TrackingSystem
This is a Python3 CLI script for tracking parcels. Works only on Linux.
It is designed for polish users, since it displays messages in polish language.
Apart from displaying brief information in command line it also uses libnotify
via gi.repository to create GNOME notifications.

## Supported postal services

* Poczta Poczta
* InPost
* UPS

## Python dependencies

* requests (http://docs.python-requests.org/en/master/)
* BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/)

## How to use

Clone, enter into the director and execute command:

**python3 track.py** __parcelNumber__

Where __parcelNumber__ is you parcel number. The script should deduce which
service to use. Every minute the state of your parcel is checked and it is
displayed in the console. If changes are detected, you are also informed via
notification. Press CTRL + C to finish script.
