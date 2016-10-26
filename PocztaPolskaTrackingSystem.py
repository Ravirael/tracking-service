from TrackingSystem import *
import requests

class PocztaPolskaTrackingSystem(TrackingSystem):
	url = 'http://mobilna.poczta-polska.pl/MobiPost/getpackage?action=getPackageData&search='

	def __init__(self, parcelNumber):
		super(PocztaPolskaTrackingSystem, self).__init__(parcelNumber)

	def getData(self):
		address = PocztaPolskaTrackingSystem.url + self.parcelNumber
		return requests.get(PocztaPolskaTrackingSystem.url + self.parcelNumber)

	def isValid(self):
		r = self.getData()
		return len(r.json()[0]) > 1

	def checkState(self):
		self.clearState()
		r = self.getData()
		js = r.json()[0]

		self.state["Numer"] = js['numer']
		self.state["Jednostka nadania"] = js['jednstkaNadania']
		self.state["Data"] = js["dataNadania"]
		self.state["Rodzaj"] = js['rodzPrzes']

		history = js['zdarzenia']
		for (i, el) in enumerate(history):
			description = el['nazwa']
			if el['przyczyna'] != 'null': description += " (%s)" % el['przyczyna']
			self.events.append(Event(el['czasZadrzenia'], el['daneSzczegJednostki'], description))
		self.events.reverse()
