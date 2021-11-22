from lotto.bills import Bills


class Ticket:
    """ This class represent a lotto ticket """
    def __init__(self, numbers, cities, ticket_type):
        self.numbers = numbers
        self.cities = cities
        self.ticket_type = ticket_type
        self.wins = 0

    def __str__(self):
        """ Printing ticket with nice ASCII table layout """
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
            space_after = (9-len(city))
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
        string += "| Type:    | "+self.ticket_type
        space_after = 9-len(self.ticket_type)
        string += " "*space_after
        string += "|\n"
        string += row
        return string

    def is_winning(self, extractions):
        """ This function check if a ticket is a winning one.
            extractions must be a list of: cityname : [list of extracted numbers]"""
        for city in self.cities:
            win_numbers_count = 0
            if self.ticket_type == "Ambata":
                for number in self.numbers:
                    if number - 1 in extractions[city]:
                        win_numbers_count += 1
                    if number in extractions[city]:
                        win_numbers_count += 1
                    if number + 1 in extractions[city]:
                        win_numbers_count += 1
            else:
                for number in self.numbers:
                    if number in extractions[city]:
                        win_numbers_count += 1
            if Bills.available_bills[self.ticket_type] <= win_numbers_count:
                return True
        return False


def main():
    """ Testing the class """
    test = Ticket([1, 7, 24, 45, 63, 78, 90], ['Roma', 'Venezia'], 'Ambo')
    print("\n" + str(test))


if __name__ == "__main__":
    main()
