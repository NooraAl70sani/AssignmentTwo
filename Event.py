class Event:
    def __init__(self, name, location, duration, price):
        self.name = name
        self.location = location
        self.duration = duration
        self.price = price

    def displayInfo(self):
        print(f"Name: {self.name}, Location: {self.location.value}, Duration: {self.duration}, Price: {self.price}")
