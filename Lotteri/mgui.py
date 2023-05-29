from tkinter import *
from tkinter import messagebox
import lotteri

# create root window
root = Tk()
root.title("Lotteri")

#create listbox
listbox = Listbox(root,
                   height=4,
                   width=30,
                   bg="white",
                   activestyle="dotbox",
                   font="helvetica",
                   fg="blue")

#Definerar storlek på fönster
root.geometry("300x300")

lotteriet = lotteri.Lotteri()

#skapar label
label_antal = Label(root, text="Antal lotter, max 3st: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

# skapar textfält
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column= 1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def update_listbox(antal_lotter):
    listbox.delete(0, END)
    listbox.insert(1, "Grattis du vann detta!")


try:
    int_antal_lotter = int(antal_lotter)
    i=0

    if (int_antal_lotter < 4):
            print("loopar")

    while i < int_antal_lotter:
            vinst = lotteriet.get_vinst()
            listbox.insert((i+2), vinst)
            i += 1


    else:
        messagebox.showinfo("Du har valt för många lotter")



    except ValueError:
    messagebox.showinfo("Endast siffror tillåtet!")


def clickSlumpButton():
    #print("tryck")
    antal_lott = textbox_antal.get()
    print("tryck! "+ antal_lott )


    #tömmer listbox
    textbox_antal.delete(0, END)
    #sätter fokus på första entryt
    textbox_antal.focus_set()
    update_listbox(antal_lott)

#skapar knapp
button_slumpa = Button(text="TUR KNAPP!", command=clickSlumpButton)
button_slumpa.grid(row=1, column=0, sticky=E, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)
root.mainloop()