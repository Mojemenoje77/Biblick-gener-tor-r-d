import tkinter as tk
from tkinter import messagebox
import random

#povzbuzení
sez1 =["Buď silný,","Věř,","Vítězství,","Výhra,","Vydržet,","Porazíš,","Náděj,","Víra,","Láska,","Dá ti odpočinutí,","Pokoj,"]
sez2 =["Musíš","Modli se","Vytrvej","Budeš mít","Dokonce","Jěště chvíli","Povstaň","Neboj se","Vysvobodí"]
#napomenutí
sez3=["Hřích,","Nereptej,","Buď pokorný,","Pýcha,","Obžerství,","Neveříci,","Nepošklebuj se,","Naslouchej Hlasu Božímu,","Vzpoura,",]
sez4= ["Nedelej","Utíkej","Nebuď","Neveříci","Modlársky","Bezcitný","Posveť se","Odpusť","Bdej","Trpěliví"]
#moudrost
sez5 =["Moudrost,","Vest slovem,","Sen,","Zjevení,","Hledat,","Pokoj,","Davej Pozor,","Buď rozumný,","V tichosti,","Chválu,","Prozíravost,"]
sez6 =["Potřebuješ","Hledej","Modli se","Dej si půst","Čti","Jednej","Hlídej","Nalez život","Vzdávej","Čekej","Bdej"]
#seznam knih a kapitol
bible = ["Žalm","EV.Jána","EV.Matúše","1 Korinťanom","Přísloví","Kazatel","Skutky apoštolú","List židúm","List Římanům","Genezis"]
kapitola =["1","2","3","4","5","6","7","8","9","10","11"]
#funkce
def generate_encouragement():
    phrase = random.choice(sez1) + " " + random.choice(sez2)
    verse = random.choice(bible) + " " + random.choice(kapitola)
    messagebox.showinfo("Povzbuzení", "Verš z Bible: " + verse + "\n Fráze: " + phrase)

def generate_warning():
    phrase = random.choice(sez3) + " " + random.choice(sez4)
    verse = random.choice(bible) + " " + random.choice(kapitola)
    messagebox.showwarning("Napomenutí", "Verš z Bible: " + verse + "\n Fráze: " + phrase)

def generate_wisdom():
    phrase = random.choice(sez5) + " " + random.choice(sez6)
    verse = random.choice(bible) + " " + random.choice(kapitola)
    messagebox.showinfo("Moudrost", "Verš z Bible: " + verse + "\n Fráze: " + phrase)

def quit_program():  #konec programu ukončení
    root.destroy()

root = tk.Tk()
root.title("Biblický Generátor") #titul
#root.geometry("400x300") #širka okna
root.minsize(width=500, height=300)
root.iconbitmap("icon.ico.ico")
root.config(bg="#C1C088")
root.resizable(False,False)



#label
greet_label = tk.Label(root, text="Biblický generátor rád", bg="#C1C088", fg="Black", font=("Franklin Gothic Medium", 18,"bold" ))
greet_label.pack(side="top")



encouragement_button = tk.Button(root,text="Povzbuzení", command=generate_encouragement, width=40, height= 10, bg="#8A894A",font=("Franklin Gothic Medium", 12,)) #tvorim tlčítka,veľkosť a farbu...
encouragement_button.pack()
warning_button = tk.Button(root, text="Napomenutí", command=generate_warning, width=40, height= 10, bg="#CE3232",font=("Franklin Gothic Medium", 12,))
warning_button.pack()
wisdom_button = tk.Button(root, text="Moudrost", command=generate_wisdom, width=40, height= 10, bg="#3255D5",font=("Franklin Gothic Medium", 12,))
wisdom_button.pack()
quit_button = tk.Button(root, text="Ukončit", command=quit_program, bg="#696C76",fg="white", width=25)
quit_button.pack()

root.mainloop()