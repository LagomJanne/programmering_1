#klass som ärver fordon

class Personbil:

    #constructor
    def __init__(self, fabrikat, color, bagagevolym):
        self.fabrikat = fabrikat
        self.color = color
        self.bagagevolym = bagagevolym

    def set_bagagevolym(self, bagagevolym):
        self.bagagevolym = bagagevolym

    def get_bagagevolym(self):
        return self.bagagevolym
    
    def print_fordon(self):
        print(self.fabrikat +", Färg: "+self.color +" Bagagevolym: " + str(self.bagagevolym))
    

