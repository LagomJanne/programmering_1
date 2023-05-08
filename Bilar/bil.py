class bil:

    #constructor körs först
    def __init__(self, fabrikat, colour, lager):
        self.fabrikat = fabrikat
        self.colour = colour
        self.lager = lager
    
    def setfabrikat(self, fabrikat):
        self.fabrikat = fabrikat

    def getfabrikat(self):
        return self.fabrikat

    def setcolour(self, colour):
        self.Colour = colour

    def getcolour(self):
        return self.Colour
    
    def setlager(self, lager):
        self.lager = lager

    def getlager(self):
        return self.lager