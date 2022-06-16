from lotto.lotto import Lotto


def main():
    """The main program, it request how many ticket to generate"""
    print("You can bet from 1 to 5 ticket, use 0 to exit")
    ticket_num = input("Hi!\nHow many ticket(s) you want to buy? ")
    while type(ticket_num) != int:
        try:
            ticket_num = int(ticket_num)
            if ticket_num < 0 or ticket_num > 5:
                print("You can bet from 1 to 5 ticket, use 0 to exit")
                ticket_num = input("How many ticket(s) you want to buy? ")
        except ValueError:
            print("Invalid input, you should write an integer number")
            ticket_num = input("How many ticket(s) you want to buy? ")
    if ticket_num == 0:
        print("Thanks! See you next time!")
        quit()
    Lotto(ticket_num)


if __name__ == "__main__":
    main()
