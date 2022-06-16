from lotto.bills import Bills


class Ticket:
    """This class represent a lotto ticket"""

    def __init__(self, numbers, cities, ticket_type, bet):
        self.numbers = numbers
        self.cities = cities
        self.ticket_type = ticket_type
        self.wins = 0
        self.bet = bet
        self.total_winning_numbers_per_city = {}
        self.money_won = 0

    def __str__(self):
        """Printing ticket with nice ASCII table layout"""
        row = "+----------+----------+\n"
        string = row
        string += "|       Numbers       |\n"
        string += row
        counter = -1
        for number in self.numbers:
            counter += 1
            if counter == 2:
                counter = 0
                string += "|\n"
            string += "|    {:02d}    ".format(number)
        if len(self.numbers) % 2 != 0:
            string += "|    --    |\n"
        else:
            string += "|\n"
        string += row

        # Adding the city
        string += "|       Cities        |\n"
        string += row
        counter = -1
        for city in self.cities:
            # Calculating the spacing before and after the word"
            space_after = 9 - len(city)
            counter += 1
            if counter == 2:
                counter = 0
                string += "|\n"
            string += "| "
            string += city.capitalize()
            for s in range(space_after):
                string += " "

        if len(self.cities) % 2 != 0:
            string += "| -------- |\n"
        else:
            string += "|\n"
        string += row

        # Adding the type of ticket
        string += "| Type:    | " + self.ticket_type
        space_after = 9 - len(self.ticket_type)
        string += " " * space_after
        string += "|\n"
        string += row

        # Adding the won prize if > 0
        if self.money_won > 0:
            string += "Money won: " + str(self.money_won)
            if self.money_won > 500:
                string += "With taxes: " + str(
                    self.money_won - ((self.money_won / 100) * 8)
                )

        return string

    def is_winning(self, extractions):
        """This function check if a ticket is a winning one.
        extractions must be a list of: cityname : [list of extracted numbers]"""
        win_numbers_count = 0
        for city in self.cities:
            if self.ticket_type == "Ambata":
                print("Ambata")
                """
                for number in self.numbers:
                    if number - 1 in extractions[city]:
                        win_numbers_count += 1
                    if number in extractions[city]:
                        win_numbers_count += 1
                    if number + 1 in extractions[city]:
                        win_numbers_count += 1
                """
            else:
                win_numbers_count = 0
                for number in self.numbers:
                    if number in extractions[city]:
                        win_numbers_count += 1
            if Bills.available_bills[self.ticket_type] <= win_numbers_count:
                print(
                    "You won on the Ruota of:",
                    city,
                    "guessing",
                    win_numbers_count,
                    "numbers right!",
                )
                self.total_winning_numbers_per_city[city] = win_numbers_count
        if len(self.total_winning_numbers_per_city) > 0:
            return True
        return False

    def _calculate_combinations(self, city):
        """This function calculate the winning combinations of the ticket"""
        import math

        n = self.total_winning_numbers_per_city[city]
        k = Bills.available_bills[self.ticket_type]
        combinations = int(
            math.factorial(n) / (math.factorial(k) - math.factorial(n - k))
        )
        print(combinations)
        return combinations

    def calculate_prize(self):
        """This function calculate the winning prize of the ticket"""
        prize_multiplier = Bills.won_matrix[self.ticket_type][len(self.numbers) - 1]
        for city in self.total_winning_numbers_per_city:
            self.money_won += self._calculate_combinations(city) * prize_multiplier


def main():
    """Testing the class"""
    test = Ticket([1, 7, 24, 45, 63, 78, 90], ["Roma", "Venezia"], "Ambo")
    test.money_won = 640
    print("\n" + str(test))


if __name__ == "__main__":

    main()
