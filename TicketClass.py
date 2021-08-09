class Ticket:
    """ This class represent a lotto ticket """
    def __init__(self, numbers, cities, ticketype):
        self.numbers = numbers
        self.cities = cities
        self.ticketype = ticketype
        self.wins = 0

    def __str__(self):
        """ Printing ticket wirh nice ASCII table layout """
        row = "+----------+----------+\n"
        string  = row
        string += "|       Numbers       |\n"
        string += row
        counter = -1
        for number in self.numbers:
            counter += 1
            if counter == 2:
                counter = 0
                string += "|\n"
            string += "|    {:02d}    ".format(number)
        if len(self.numbers)%2 != 0:
            string += "|    --    |\n"
        else:
            string +="|\n"
        string += row
    
        #Adding the city
        string += "|       Cities        |\n"
        string += row
        counter = -1
        for city in self.cities:
            #calculating the spacing before and after the word"
            spaceafter = (9-len(city))
            counter += 1
            if counter == 2:
                counter = 0
                string += "|\n"
            string += "| "
            string += city.capitalize()
            for s in range(spaceafter):
                string += " "
            
        if len(self.cities)%2 != 0:
            string += "| -------- |\n"
        else:
            string += "|\n"
        string += row

        #Adding the type of ticket
        string += "| Type:    | "+self.ticketype
        spaceafter = 9-len(self.ticketype)
        string += " "*spaceafter
        string += "|\n"
        string += row
        return string
        
def main():
    """ Testing the class """
    test = Ticket([1,5,12,54,67], ["Roma", "Milano", "Bari", "Firenze","Cagliari"])
    print(test)

if __name__=="__main__":
    main()