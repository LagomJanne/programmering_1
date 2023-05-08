import elevhandler

looping = True
elevhand = elevhandler.Elevhandler()

while looping:

    val = elevhand.print_meny()
    if val == "1":
        print ("val 1")

    elif val == "2":
        print ("val 2")

    elif val == "3":
        print ("val 3")

    elif val == "4":
        break

