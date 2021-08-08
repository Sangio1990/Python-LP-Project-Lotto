class Ticket:
    """ This class represent a lotto ticket """
    def __init__(self, numbers, cities):
        self.numbers = numbers
        self.cities = cities
        self.wins = 0

    def __str__(self):
        string = "Cities : "
        for city in self.cities:
            string += city.capitalize()+" "
        string += "\nNumbers: "
        for num in self.numbers:
            string += str(num)+" "
        return string

    
    
        
def main():
    """ Testing the class """
    test = Ticket([1,5,12,54,67], ["Roma", "Milano"])
    print(test)

if __name__=="__main__":
    main()