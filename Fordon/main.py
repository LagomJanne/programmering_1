import lastbil
import personbil

looping = True

Merchedos_gul = personbil.Personbil("Merchedos", "Gul", 5)
Cittohträn_rosa = personbil.Personbil("Cittohträn", "Rosa", 14)

LämnaTillbaka_grön = lastbil.Lastbil("LämnaTillbaka", "Grön", 3)
Ska_ska_ska_FortniteBattelpass_lila = lastbil.Lastbil("Ska,ska,ska....FortniteBattlepass", "Lila", 0.4)

personbils_lista = [Merchedos_gul, Cittohträn_rosa]
lastbils_lista = [LämnaTillbaka_grön, Ska_ska_ska_FortniteBattelpass_lila]

def print_fordonslista(fordonslista):

    for ettfordon in fordonslista:
        print(ettfordon.fabrikat +" Typ="+ str(type(ettfordon)))


        if(isinstance(ettfordon   ,personbil.Personbil)):
            print(ettfordon.fabrikat +" Färg: "+ ettfordon.color + ", Flakvolym: " + str(ettfordon.flakvolym) + "L")  

        elif (isinstance(ettfordon,personbil.Personbil)):
            print(ettfordon.fabrikat +" Färg: "+ ettfordon.color + ", Bagagevolym: "+ str(ettfordon.bagagevolym) +  "L")


def print_fordonslista(fordonslista):

    for ettfordon in fordonslista:
        ettfordon.print_fordon() 




while looping:
    print("---------------------------------------------------")
    print("\n-:Klasser och arv av fordon:-\n")

    val_fordon = input("Vilken fordonstyp vill du lista? 1=lastbilar  :  2=personbilar: ")


    if (val_fordon == "1"):
        print("\n-:Lastbilar:-")
        print("-------------------------------------------------")
        print_fordonslista(lastbils_lista)

    elif (val_fordon == "2"):
        print("\n-:PersonBilar:-")
        print("--------------------------------------------")
        print_fordonslista(personbils_lista)

    else:
        print("\nOgiltigt val")

    print("----------------------------------------------")
    go = input("\n Vill du lista fordon igen? j/n ")
    print("\n")

    if (go == "n"):
        break

