class Event:
    def __init__(self, name, location, duration, price):
        self.name = name
        self.location = location
        self.duration = duration
        self.price = price

    def displayInfo(self):
        print(f"Name: {self.name}, Location: {self.location.value}, Duration: {self.duration}, Price: {self.price}")

    def setName(self, name):
        self.name = name

    def setLocation(self, location):
        self.location = location

    def setDuration(self, duration):
        self.duration = duration

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getDuration(self):
        return self.duration

    def getPrice(self):
        return self.price
