class Artwork:
    def __init__(self, title, artist, dateOfCreation, historicalSignificance, location):
        self.title = title
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance
        self.location = location

    def displayInfo(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Date of Creation: {self.dateOfCreation}, "
              f"Historical Significance: {self.historicalSignificance}, Location: {self.location.value}")

    def setTitle(self, title):
        self.title = title

    def setArtist(self, artist):
        self.artist = artist

    def setDateOfCreation(self, dateOfCreation):
        self.dateOfCreation = dateOfCreation

    def setHistoricalSignificance(self, historicalSignificance):
        self.historicalSignificance = historicalSignificance

    def setLocation(self, location):
        self.location = location

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def getDateOfCreation(self):
        return self.dateOfCreation

    def getHistoricalSignificance(self):
        return self.historicalSignificance

    def getLocation(self):
        return self.location
