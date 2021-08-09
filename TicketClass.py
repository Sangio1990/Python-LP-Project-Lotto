class Ticket:
    """ This class represent a lotto ticket """
    def __init__(self, numbers, cities, typeofticket):
        self.numbers = numbers
        self.cities = cities
        self.typeofticket = typeofticket
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
    
        #Adding the city
        string += row   
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
            string += " "*spaceafter
            
        if len(self.cities)%2 != 0:
            string += "| -------- |\n"
        else:
            string += "|\n"
        
        #Adding the type of ticket
        string += row
        string += "| Type:    | "+self.typeofticket
        spaceafter = 9-len(self.typeofticket)
        string += " "*spaceafter
        string += "|\n"
        string += row
        return string
        
def main():
    """ Testing the class """
    test = Ticket([1,5,12,54,67], ["Roma", "Milano", "Bari", "Firenze","Cagliari"], "Cinquina")
    print(test)

if __name__=="__main__":
    main()