import random

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer!")

frukter =("Banan", "Äpple", "Päron", "Avokado", "Bapelsin")

looping = True

while looping:

    print("-----------------------")
    print("\n-:FruktAutomat:-\n")

    i=1

    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1


    fruktnr = input("\nMata in siffra för vald frukt: ")
    print_fruit(fruktnr)
    
    go = input("Vill du välja en frukt till?")

    if (go == "n"):
        break

print("\n-----------------------------\n")
print("Föresten här får du en frukt till! ")
slumpfrukt = random.radiant(1,5)
print_fruit(slumpfrukt)