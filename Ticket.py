from VisitorCategory import VisitorCategory

class Ticket:
    VAT = 0.05

    def __init__(self, event, visitorCategory, groupSize):
        self.event = event
        self.visitorCategory = visitorCategory
        self.groupSize = groupSize

    def setEvent(self, event):
        self.event = event

    def setVisitorCategory(self, visitorCategory):
        self.visitorCategory = visitorCategory

    def setGroupSize(self, groupSize):
        self.groupSize = groupSize

    def getEvent(self):
        return self.event

    def getVisitorCategory(self):
        return self.visitorCategory

    def getGroupSize(self):
        return self.groupSize

    def calculatePrice(self):
        base = self.event.price

        if self.visitorCategory == VisitorCategory.Adult:
            ticketPrice = base
        elif self.visitorCategory == VisitorCategory.Child or self.visitorCategory == VisitorCategory.Student or self.visitorCategory == VisitorCategory.Senior:
            ticketPrice = 0.0
        elif self.visitorCategory == VisitorCategory.Group:
            ticketPrice = base * self.groupSize * 0.5
        else:
            ticketPrice = base

        ticketPrice += ticketPrice * self.VAT

        return ticketPrice
