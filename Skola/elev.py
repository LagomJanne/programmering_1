
class Elev:
    def __init__(self, namn, utbildning, tel):
        self.namn = namn
        self.utbildning = utbildning
        self.tel = tel

    def get_elev(self):
        svar = self.namn+ " | Program: " +self.uttbildning+ " |"