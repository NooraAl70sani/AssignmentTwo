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
