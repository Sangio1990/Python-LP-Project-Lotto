class Cities:
    """This class represent tha available city where the user can bet"""

    available_city = [
        "Bari",
        "Cagliari",
        "Firenze",
        "Genova",
        "Milano",
        "Napoli",
        "Palermo",
        "Roma",
        "Torino",
        "Venezia",
    ]

    @staticmethod
    def valid_city(city):
        """Check if a city is available for bet"""
        if city.lower().capitalize() in Cities.available_city:
            return True
        else:
            return False

    @staticmethod
    def format_city(city):
        """Return the formatted string for the choosen city"""
        return city.lower().capitalize()
