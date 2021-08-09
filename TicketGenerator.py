import TicketClass
import random

def TicketGenerator():
    """ This function create a ticket and return that ticket """
    
    #Choosing the numbers
    numbers = []
    stop = False
    while not stop:
        numberstobet = input("How many numbers you wanna bet: ")
        try:
            numberstobet = int(numberstobet)
            if numberstobet < 1 or numberstobet > 10:
                print("The number must be an integer between 1 and 10")
            else:
                stop = True
        except ValueError:
            print("You must write an integer number")
    for n in range(numberstobet):
        stop = False
        while not stop:
            number = random.randint(1,90)
            if number not in numbers:
                numbers.append(number)
                stop = True
                
    #Choosing the cities
    print("\nNow choose the cities:")
    stop = False
    cities = []
    avaible_cities = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]
    print("Leave blank to stop choosing.")
    while not stop:
        print("\nAvaible cities:")
        for city in avaible_cities:
            print(city+" ", end = "")
        choosen = input("\nOn which one you banna bet? ")
        choosen = choosen.lower().capitalize()
        if choosen == "":
            stop = True
        elif choosen in avaible_cities:
            cities.append(choosen)
            avaible_cities.remove(choosen)
            if len(avaible_cities) == 0:
                stop = True
        else:
            print("City not avaible or incorrect.")
            
    #Choosing the type of ticket
    avaiable_type = ["Ambata", "Ambo", "Terno", "Quaterna", "Cinquina"]
    print("\nThe type of ticket avaiable are: ")
    for ttype in avaiable_type:
        print(ttype,"", end="")
    stop = False
    while not stop:
        ticketype = input("\nChoose the type of the ticket: ").lower().capitalize()
        if ticketype == "":
            stop = True
        elif ticketype not in avaiable_type:
            print("You must choose one of the ticket type above, try again:")
        else:
            stop = True

    #Checking that ticket is not empty
    if len(numbers) == 0 or len(cities) == 0 or ticketype == "" :
        print("Ticket canceled")
        return False
    
        #Returng the new generated ticket
    return TicketClass.Ticket(numbers, cities, ticketype)

def main():
    """ Testing the functions """
    test = TicketGenerator()
    print(test)

if __name__=="__main__":
    main()