class Bills:
    """This class represent the available type of bill"""

    available_bills = {"Ambata": 1, "Ambo": 2, "Terno": 3, "Quaterna": 4, "Cinquina": 5}

    won_matrix = {
        "Ambata": [11.23, 5.61, 3.74, 2.80, 2.24, 1.87, 1.60, 1.40, 1.24, 1.12],
        "Ambo": ["-", 250, 83.33, 41.66, 25, 16.66, 11.90, 8.92, 6.94, 5.55],
        "Terno": ["-", "-", 4500, 1125, 450, 225, 128.57, 80.35, 53.57, 37.50],
        "Quaterna": [
            "-",
            "-",
            "-",
            120000,
            24000,
            8000,
            3428.57,
            1714.28,
            952.38,
            571.42,
        ],
        "Cinquina": [
            "-",
            "-",
            "-",
            "-",
            6000000,
            1000000,
            285714.28,
            107142.85,
            47619.04,
            23809.52,
        ],
    }

    @staticmethod
    def valid_bill(bill, available_ticket_type):
        """Return if the bill type is a valid one"""
        if bill in available_ticket_type:
            return True
        else:
            return False

    @staticmethod
    def format_bill(bill):
        """Return the right formatted text of the chosen bill"""
        return bill.lower().capitalize()

    @staticmethod
    def available_ticket_type(numbers_to_bet: int) -> list:
        """Return a list with the avaiable ticket type"""
        available_ticket_type = []
        for ttype in Bills.available_bills:
            if numbers_to_bet >= Bills.available_bills[ttype]:
                available_ticket_type.append(ttype)
        return available_ticket_type
