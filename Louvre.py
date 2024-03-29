from Artwork import Artwork
from Exhibition import Exhibition
from Event import Event
from Location import Location
from VisitorCategory import VisitorCategory
from User import User
from Ticket import Ticket

class Louvre:
    def __init__(self):
        self.users = []

    def main(self):
        while True:
            try:
                choice = input("Are you an existing user? (yes/no): ").lower()
                if choice not in ['yes', 'no']:
                    raise ValueError("Invalid choice. Please enter 'yes' or 'no'.")
            except ValueError as ve:
                print(ve)
                continue

            if choice == 'yes':
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                foundUser = next(
                    (user for user in self.users if user.username == username and user.password == password), None)

                if foundUser:
                    print("Login successful!")
                    while True:
                        try:
                            print("\nOptions:")
                            print("1. Artwork Management")
                            print("2. Ticketing and Pricing")
                            print("3. View Purchased Tickets and Bills")
                            print("4. Logout")
                            print("-----")

                            subChoice = input("Enter your choice: ")
                            if subChoice not in ['1', '2', '3', '4']:
                                raise ValueError("Invalid choice. Please enter a number between 1 and 4.")
                        except ValueError as i:
                            print(i)
                            continue

                        if subChoice == '1':
                            self.manageArtworks(foundUser)
                        elif subChoice == '2':
                            self.manageTickets(foundUser)
                        elif subChoice == '3':
                            self.viewPurchasedTicketsAndBills(foundUser)
                        elif subChoice == '4':
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Please try again.")

                else:
                    print("Failed to log in.")

            elif choice == 'no':
                username = input("Enter a new username: ")
                password = input("Enter a new password: ")
                self.users.append(User(username, password))
                print("Signup successful!")
                continue

            logoutChoice = input("Do you want to exit? (yes/no): ").lower()
            if logoutChoice == 'yes':
                print("Thank you for connecting with Louvre, See you next time!")
                break

    def manageArtworks(self, user):
        print("Artwork Management:")
        print("1. Add New Artwork")
        print("2. Display All Artworks")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.addArtwork(user)
        elif choice == '2':
            self.displayArtworks(user)
        else:
            print("Invalid choice.")

    def addArtwork(self, user):
        try:
            print(" ")
            title = input("Enter artwork title: ")
            artist = input("Enter artist name: ")
            dateOfCreation = input("Enter date of creation: ")
            historicalSignificance = input("Enter historical significance: ")
            location = input("Enter artwork location (PermanentGalleries, ExhibitionHalls, OutdoorSpaces): ")
            if location not in Location.__members__:
                raise ValueError("Invalid location.")
        except ValueError as i:
            print(i)
            return

        artwork = Artwork(title, artist, dateOfCreation, historicalSignificance, Location[location])
        user.artworks.append(artwork)
        print(" ")
        print("Artwork added successfully!")

    def displayArtworks(self, user):
        if not user.artworks:
            print("No artworks to display.")
        else:
            for artwork in user.artworks:
                artwork.displayInfo()
    def manageTickets(self, foundUser):
        print("Ticketing and Pricing:")
        print("1. View Ticket Prices")
        print("2. Purchase Ticket")
        print(" ")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("------")
            print("Ticket Prices:")
            print("1. Adult (Ages 18 to 60): 63 AED")
            print("2. Child (Below 18): Free")
            print("3. Teacher/Student/Senior: Free")
            print("4. Group (50% Discount)")
            print("5. Special Events (Individual Prices)")
            print(" ")
        elif choice == '2':
            try:
                eventName = input("Enter event name: ")
                print(" ")
                eventLocation = input("Enter event location: ")
                print(" ")
                eventDuration = input("Enter event duration: ")
                print(" ")
                eventPrice = float(input("Enter event price: "))
                visitorCategory = input(
                    "Enter visitor category (Adult/Child/Teacher/Student/Senior/Group): ").capitalize()
                print(" ")
                if visitorCategory not in VisitorCategory.__members__:
                    raise ValueError("Invalid visitor category.")
            except ValueError as ve:
                print(ve)
                return

            if visitorCategory == 'Group':
                try:
                    groupSize = int(input("Enter group size: "))
                    if groupSize <= 0:
                        raise ValueError("Group size must be a positive integer.")
                except ValueError as ve:
                    print(ve)
                    return

                ticket = Ticket(Event(eventName, eventLocation, eventDuration, eventPrice),
                                VisitorCategory[visitorCategory], groupSize)
            else:
                ticket = Ticket(Event(eventName, eventLocation, eventDuration, eventPrice),
                                VisitorCategory[visitorCategory], groupSize=None)

            ticketPrice = ticket.calculatePrice()
            print(f"Ticket price (including VAT): {ticketPrice} AED")
            foundUser.tickets.append(ticket)
        else:
            print("Invalid choice.")

    def viewPurchasedTicketsAndBills(self, user):
        print("Purchased Tickets and Bills:")
        if not user.tickets:
            print("No purchased tickets.")
        else:
            for i, ticket in enumerate(user.tickets, start=1):
                print(f"Ticket {i}:")
                print(" ")
                print(f"Event: {ticket.event.name}")
                print(" ")
                print(f"Visitor Category: {ticket.visitorCategory.name}")
                print(" ")
                if ticket.groupSize is not None:
                    print(f"Group Size: {ticket.groupSize}")
                    print(" ")
                print(f"Price (including VAT): {ticket.calculatePrice()} AED")
                print(" ")
