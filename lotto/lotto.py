import random

from lotto.bills import Bills
from lotto.cities import Cities
from lotto.ticket import Ticket


class Lotto:
    """This class is the business logic of the program"""

    def __init__(self, n):
        self.tickets = []
        self.ticket_n = n
        self.extractions = {}

        for x in range(self.ticket_n):
            print("\nTime to choose for the ticket number", x + 1)
            self.tickets.append(Lotto.create_ticket())

        # Extracting the numbers for every city
        self.extraction()
        print(
            self.extractions
        )  # This is only for debugging purpose, can be deleted later on
        winning_ticket = []
        for ticket in self.tickets:
            if ticket.is_winning(self.extractions):
                winning_ticket.append(ticket)

        if len(winning_ticket) > 0:
            print("The winning ticket(s):")
            for ticket in winning_ticket:
                ticket.calculate_prize()
                print(ticket)
        else:
            print("No ticket result as winning, better luck next time!")

    @staticmethod
    def create_ticket():
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
        numbers = Lotto.number_generator(numbers_to_bet)

        # Choosing the cities
        print("\nNow choose the cities:")
        stop = False
        available_city = [i for i in Cities.available_city]
        print(
            "Leave blank to stop choosing.\n"
            "If you wanna bet an all cities write: All"
        )
        cities = []
        while not stop:
            print("\nAvailable cities:")
            for city in available_city:
                print(city + " ", end="")
            chosen = input("\nOn which one you wanna bet? ")
            if chosen == "" and len(cities) > 0:
                stop = True
            elif chosen.lower() == "all":
                cities = Cities.available_city
                stop = True
            elif Cities.valid_city(chosen):
                cities.append(Cities.format_city(chosen))
                available_city.remove(Cities.format_city(chosen))
                if len(available_city) == 0:
                    stop = True
            else:
                print("City not available or incorrect.")
        cities.sort()

        # Choosing the type of ticket
        print("\nYou can choose one type of ticket.")
        print("The type of ticket available are: ")
        available_ticket_type = Bills.available_ticket_type(numbers_to_bet)
        print(" ".join(available_ticket_type))
        stop = False
        while not stop:
            ticket_type = (
                input("\nChoose the type of the ticket: ").lower().capitalize()
            )
            if not Bills.valid_bill(ticket_type, available_ticket_type):
                print("You must choose one of the ticket type from above, try again:")
            else:
                stop = True
        ticket_type = Bills.format_bill(ticket_type)

        # Choosing the import to bet
        print("\nNow choose the import to bet:")
        stop = False
        while not stop:
            ticket_import = input("How much you wanna bet on this ticket? ")
            try:
                ticket_import = int(ticket_import)
                stop = True
            except ValueError:
                try:
                    ticket_import = float(ticket_import)
                    stop = True
                except ValueError:
                    print("Invalid value, you must put a number.")

        return Ticket(numbers, cities, ticket_type, ticket_import)

    @staticmethod
    def number_generator(numbers_to_bet):
        """This function generate a random number and check if it is already in the list"""
        numbers = []
        for n in range(numbers_to_bet):
            stop = False
            while not stop:
                number = random.randint(1, 90)
                if number not in numbers:
                    numbers.append(number)
                    stop = True
        numbers.sort()
        return numbers

    def extraction(self):
        for city in Cities.available_city:
            temp_extraction = []
            stop = False
            while not stop:
                num = random.randint(1, 91)
                if num not in temp_extraction:
                    temp_extraction.append(num)
                    if len(temp_extraction) == 5:
                        stop = True
            self.extractions[city] = temp_extraction


if __name__ == "__main__":
    test = Lotto.create_ticket()
    print(test)
