import TicketClass
import TicketCreator

def main():
    """ The main program, it request how many ticket to generate """
    TicketNum = input("Hi!\nHow many ticket(s) you want to buy? ")
    while type(TicketNum) != int:
        try:
            TicketNum = int(TicketNum)
        except:
            print("Invalid input, you should write an integer number")
            TicketNum = input("How many ticket(s) you want to buy? ")
    if TicketNum == 0:
        print("Thanks! See you next time!")
        quit()
    tickets = dict()
    #Creating the number of requested Ticket
    for x in range(TicketNum):
        print("\nTime to choose for the ticket number",x+1)
        tickets[x+1] = TicketCreator.TicketCreation()
    
    #testing
    print("\nPrinting ticket:")
    for ticket in tickets:
        if tickets[ticket] == False:
            print("Something went wrong, try again")
            quit()
        print("")
        print("+----------+----------+")
        print("|  Ticket  |    ",ticket,"   |")
        print(tickets[ticket])        

if __name__=="__main__":
    main()