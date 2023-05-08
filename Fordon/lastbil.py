class Lastbil:
    
    def __init__(self, fabrikat, color, flakvolym):
        self.fabrikat = fabrikat
        self.color = color
        self.flakvolym = flakvolym


    def set_flakvolym(self, flakvolym):
        self.flakvolym = flakvolym

    def get_flakvolym(self):
        return self.flakvolym
    
    def print_fordon(self):
        print(self.fabrikat + " Färg: " + self.color + " flakvolym: " + str(self.flakvolym))
        