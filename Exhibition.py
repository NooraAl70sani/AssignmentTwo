class Exhibition:
    def __init__(self, name, duration, location):
        self.name = name
        self.duration = duration
        self.location = location

    def displayInfo(self):
        print(f"Name: {self.name}, Duration: {self.duration}, Location: {self.location.value}")

    def setName(self, name):
        self.name = name

    def setDuration(self, duration):
        self.duration = duration

    def setLocation(self, location):
        self.location = location

    def getName(self):
        return self.name

    def getDuration(self):
        return self.duration

    def getLocation(self):
        return self.location
