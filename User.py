class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.artworks = []
        self.tickets = []

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setArtworks(self, artworks):
        self.artworks = artworks

    def setTickets(self, tickets):
        self.tickets = tickets

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getArtworks(self):
        return self.artworks

    def getTickets(self):
        return self.tickets

