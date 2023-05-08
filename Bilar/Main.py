import bil

looping = True

Ford_red = bil.bil("Ford", "Röd", 5)
Volvo240_rosa = bil.bil("Volvo240", "Rosa", 1)
Ferrari_röd = bil.bil("Ferrari", "Röd", 20)

billista = [ Ford_red, Volvo240_rosa, Ferrari_röd]


while looping:
    print("------------------------------------")
    print("BilAutomat")

    i=0

    for bil in billista:

        print(str(i+1) + " : " + bil.fabrikat + " Färg: " + bil.colour + " Lager: " + str(bil.lager))
        i=i+1

    bil_nr = input("\n Mata in siffra för vald bil: ")
    bil_nr_int = int(bil_nr)

    lager_int = billista[bil_nr_int-1].getlager()
    lager_string = str(lager_int)

    if lager_int > 0:
        print("\n En " + billista[bil_nr_int-1].colour + " " + billista[bil_nr_int-1].fabrikat + " Kommer här!")

        #minskar lager
        nyttlagersaldo_int = lager_int - 1
        nyttlagersaldo_str = str(nyttlagersaldo_int)

        billista[bil_nr_int-1].setlager(nyttlagersaldo_int)

    else:
        print("Tyvärr slut på vald bil")

    print("----------------------------------------------")
    print("\nLagersaldo före: " +lager_string+ " st")
    print("Lagersaldo efter: " + nyttlagersaldo_str + " st")


    svar = input("\n Vill du avsluta programmet? j/n : ")
    if (svar == 'j'):
        break