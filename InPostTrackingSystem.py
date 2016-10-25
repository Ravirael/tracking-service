from TrackingSystem import *
import requests

class InPostTrackingSystem(TrackingSystem):
	url = 'https://tracking.inpost.pl/api/v1/history/package[0]='

	def __init__(self, parcelNumber):
		super(InPostTrackingSystem, self).__init__(parcelNumber)

	def getData(self):
		address = InPostTrackingSystem.url + self.parcelNumber
		headers = {'origin' : 'https://inpost.pl'}
		return requests.get(address, headers = headers)

	def isValid(self):
		try:
			js = self.getData().json()
			js['maxStatusCode']
			return True
		except:
			return False

	def checkState(self):
		self.clearState()
		js = self.getData().json()

		currentIndex = js['maxStatusCode']
		history = js['history']
		currentState = history[currentIndex]

		self.state["Numer"] = self.parcelNumber
		self.state["Typ"] = js["typeOfParcel"]

		for (i, index) in enumerate(history):
			event = Event(history[index]['changeDate'], '', history[index]['pl_desc'])
			self.events.append(event)
