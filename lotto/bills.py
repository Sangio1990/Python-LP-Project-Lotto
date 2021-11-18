class Bills:
    """ This class represent the available type of bill """
    available_bills = ["Ambata", "Ambo", "Terno", "Quaterna", "Cinquina"]

    @staticmethod
    def valid_bill(bill):
        """ Return if the bill type is a valid one """
        if bill in Bills.available_bills:
            return True
        else:
            return False

    @staticmethod
    def format_bill(bill):
        """ Return the right formatted text of the choosen bill"""
        return bill.lower().capitalize()
