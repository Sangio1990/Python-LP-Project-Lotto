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
        print("Time to choose for the ticket number",x+1)
        tickets[x] = TicketCreator()
    
    #testing
    for ticket in tickets: 
        print(ticket)
    


if __name__=="__main__":
    main()