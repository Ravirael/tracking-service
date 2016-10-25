from TrackingSystem import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

class UPSTrackingSystem(TrackingSystem):
    url = 'https://www.ups.com/WebTracking/processInputRequest?loc=pl_PL&Requester=NES&tracknum='

    def __init__(self, parcelNumber):
        super(UPSTrackingSystem, self).__init__(parcelNumber)

    def getData(self):
        address = UPSTrackingSystem.url + self.parcelNumber
        return urlopen(address).read()

    def isValid(self):
        self.clearState()
        site = BeautifulSoup(self.getData(), "lxml")
        return len(site.select(".dataTable")) > 0

    def checkState(self):
        self.clearState()
        site = BeautifulSoup(self.getData(), "lxml")
        table = site.select(".dataTable")[0]
        table = table.find_all("tr")[1:]

        self.state["Numer"] = self.parcelNumber
        #Thats radical!
        self.state["Planowane doręczenie"] = site.find("label", text = "Planowane doręczenie:").find_parent().find_parent().find("dd").text

        for row in table:
            data = row.find_all("td")
            data = list(map(lambda x: " ".join(x.text.split()), data))
            self.events.append(Event("%s %s" % (data[1], data[2]), data[0], data[3]))
