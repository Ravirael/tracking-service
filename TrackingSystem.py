import abc

class Event:
	def __init__(self, date, place, description):
		self.date = date
		self.place = place
		self.description = description

	def __str__(self):
		event = ""
		if len(self.date) > 0: event += "[%s] " % self.date
		if len(self.place) > 0: event += "[%s] " % self.place
		return event + self.description

class TrackingSystem:
	def __init__(self, parcelNumber):
		self.events = []
		self.state = {}
		self.parcelNumber = parcelNumber;

	@abc.abstractmethod
	def isValid(self):
		'''Returns whether the parcel number is valid'''
		return

	@abc.abstractmethod
	def checkState(self):
		'''Returns whether the parcel number is valid'''
		return

	def clearState(self):
		self.events = []
		self.state = {}
