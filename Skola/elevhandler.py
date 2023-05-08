

class Elevhandler:
    
    def __init__(self):
        self.elevlista = []
        self.filnamn = "elever.pkl"

    def print_meny(self):
        
        print ("\n *            *     *           *        *\n*  *      *          *        *     *\n   *          *        *    *      \n~~~~~~~~~~~MENY~~~~~~~~~~~")
        print ("|                        |")
        print ("|   1. Lista elever      |\n|   2. Lägg till elev    |\n|   3. Ta bort elev      |\n|   4. Avsluta           |")
        print ("|                        |")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        val = input ("Mata in ditt val: ")
        return val
