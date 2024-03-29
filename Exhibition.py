class Exhibition:
    def __init__(self, name, duration, location):
        self.name = name
        self.duration = duration
        self.location = location

    def displayInfo(self):
        print(f"Name: {self.name}, Duration: {self.duration}, Location: {self.location.value}")
