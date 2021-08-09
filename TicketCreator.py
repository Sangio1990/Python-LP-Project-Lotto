import TicketClass

def TicketCreation():
    """ This function create a ticket and return that ticket """
    
    #Choosing the numbers
    numbers = []
    number = input("To stop choosing numbers just leave blank.\nChoose the first number: ")
    numcounter = 1
    while number != "":
        try:
            number = int(number)
            if number < 1 or number > 90:
                print("You must choose a number between 1 an 90")
                number = input("Choose the next number: ")
            elif number in numbers:
                print("You have already choosen this number.")
                number = input("Choose the next number: ")
            elif numcounter == 10:
                print("You reached the max limit of number choise, now it's time for the city!")
                numbers.append(number)
                number = ""
            else:
                numcounter += 1
                numbers.append(number)
                number = input("Choose the next number: ")
        except ValueError:
            print("You must insert an integer number from 1 to 90")    
            number = input("Choose the next number: ")
    
    #Choosing the cities
    print("\n\nNow choose the cities:")
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

    if len(numbers) == 0 or len(cities) == 0 or ticketype == "":
        print("Ticket canceled")
        return False
    #Returng the new generated ticket
    return TicketClass.Ticket(numbers, cities, ticketype)

def main():
    """ Testing the functions """
    test = TicketCreation()
    print(test)

if __name__=="__main__":
    main()