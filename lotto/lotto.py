import random

from lotto.bills import Bills
from lotto.cities import Cities
from lotto.ticket import Ticket


class Lotto:
    """ This class is the business logic of the program """
    def __init__(self):
        self.numbers = []
        self.cities = []
        self.ticket_type = ""

    def create_ticket(self):
        # Choosing the numbers
        stop = False
        while not stop:
            numbers_to_bet = input("How many numbers you wanna bet: ")
            try:
                numbers_to_bet = int(numbers_to_bet)
                if numbers_to_bet < 1 or numbers_to_bet > 10:
                    print("The number must be an integer between 1 and 10")
                else:
                    stop = True
            except ValueError:
                print("You must write an integer number")
        self.number_generator(numbers_to_bet)

        # Choosing the cities
        print("\nNow choose the cities:")
        stop = False
        available_city = [i for i in Cities.available_city]
        print("Leave blank to stop choosing.\n"
              "If you wanna bet an all cities write: Tutte")
        while not stop:
            print("\nAvailable cities:")
            for city in available_city:
                print(city + " ", end="")
            choosen = input("\nOn which one you wanna bet? ")
            if choosen == "":
                stop = True
            elif choosen == "Tutte":
                self.cities = Cities.available_city
                stop = True
            elif Cities.valid_city(choosen):
                self.cities.append(Cities.format_city(choosen))
                available_city.remove(choosen)
                if len(available_city) == 0:
                    stop = True
            else:
                print("City not available or incorrect.")
        self.cities.sort()

        # Choosing the type of ticket
        print("\nYou can choose one type of ticket.")
        print("The type of ticket available are: ")
        for ttype in Bills.available_bills:
            print(ttype, "", end="")
        stop = False
        while not stop:
            ticket_type = input("\nChoose the type of the ticket: ").lower().capitalize()
            if not Bills.valid_bill(ticket_type):
                print("You must choose one of the ticket type from above, try again:")
            else:
                stop = True
        self.ticket_type = Bills.format_bill(ticket_type)

        return Ticket(self.numbers, self.cities, self.ticket_type)

    def number_generator(self, numbers_to_bet):
        """ This function generate a random number and check if it is already in the list"""
        for n in range(numbers_to_bet):
            stop = False
            while not stop:
                number = random.randint(1, 90)
                if number not in self.numbers:
                    self.numbers.append(number)
                    stop = True
        self.numbers.sort()
