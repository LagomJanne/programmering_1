import random
print("\n.:GissaTalet:.\n\n")

print("Gissa 3 st gånger och du kan vinna en anka")
slumptal = random.randint(1, 10)
antalgissningar = 1
vinst = False

print(slumptal)

while antalgissningar <4 :
    antalgissningar = antalgissningar +1
    spelarensval = input("Gissa ett tal")


    if slumptal == int(spelarensval):
        print("Du Vann en anka")
        vinst = True
        break

if vinst == False:
    print("\n\nTyvärr det blev ingen Anka denna gång\n")




