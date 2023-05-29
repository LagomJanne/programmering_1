import os
import jokehandler



def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n-Förläng livet med skratt och en rolig hiastoria-")

    url = f"https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"

    nr = 1

    jokeobjekt = jokehandler.Jokehandler(url)

    while True:

        t_joke = jokeobjekt.get_joke()

        if (nr)>99:
            print(f"\n{nr}.------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif (nr)<10:
            print(f"\n{nr}.--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print(f"\n{nr}.-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"{t_joke}")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        nr += 1

        entill = input("Vill du höra ett skämt till? j/n \n\n")

        if(entill == "n" or entill == "N"):
            break

main()
