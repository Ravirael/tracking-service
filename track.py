import requests
from html.parser import HTMLParser
import time
import os
import platform
import sys
from gi.repository import Notify

from TrackingSystem import *
from PocztaPolskaTrackingSystem import PocztaPolskaTrackingSystem
from InPostTrackingSystem import InPostTrackingSystem
from UPSTrackingSystem import UPSTrackingSystem


def getParcelNumber():
	return sys.argv[1]

prevHistoryLen = 0
Notify.init("Przesyłka")
sub = TrackingSystem.__subclasses__()

for cl in sub:
	trackingSystem = cl(getParcelNumber())
	if trackingSystem.isValid(): break

while True:
	os.system("clear")
	print("Stan na %s\n" % time.ctime())

	trackingSystem.checkState()
	for (key, value) in trackingSystem.state.items():
		print("%s: %s" % (key, value))

	print()

	padding = 40*'-'
	print(padding+'ZDARZENIA'+padding)

	for (i, event) in enumerate(trackingSystem.events):
		data = str(i + 1)+". [%s] [%s] %s" % (event.date, event.place, event.description)
		print(data)

	if len(trackingSystem.events) > prevHistoryLen:
		Notify.Notification.new ("Nowy stan przesyłki %s" % trackingSystem.parcelNumber,
                               str(trackingSystem.events[0]),
                               "dialog-information").show()
	prevHistoryLen = len(trackingSystem.events)
	time.sleep(60)
