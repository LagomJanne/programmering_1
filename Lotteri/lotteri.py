import random

class Lotteri:

    def __init__(self) :

        self.list_vinster = [
            "10693g plast", 
            "Ett bordsben", 
            "Bra skum",
            "Dåligt skum", 
            "Ett bord utan ben",
            "1kg is",
            "1m^2 land i Dalarna",
            "En 20mm case fan",
            "472g av okänt radioaktivt material",
            "2kg sand från sahara",
            "En byggarbetare från Belgien",
            "5kg badsalt", 
            "En tom konservburk",
            "En hemlös gubbes hoodie",
            "En kristen tant",
            "En påse med blodpudding",
            "Ett barn i en nutellaburk",
            "En halv bil",
            "Ett papper med en QR-kod",
            "En kompis från polen som äter tegelsten"
            ]
        
    def get_vinst(self):
        slumptal = random.randint(0,19)
        return self.list_vinster[slumptal]