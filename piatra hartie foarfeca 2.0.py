#Importăm Tkinker ca modul
from tkinter import * 

#-------------------------------------------------------#PARTEA 1----------------------------------------------------------------------------------
#Adăugăm 2 variabile, jucător 1 și jucător 2
jucator1 = "piatră, hârtie, foarfecă"
jucator2 = "piatră, hârtie, foarfecă"

#facem funcția de joc
def joc():
        if str(jucator1.get()) == "piatră" and str(jucator2.get()) == "hârtie":
            rezultat.set(print("jucator2 căștigă, hârtia bate piatră"))
        elif str(jucator1.get()) == "piatră" and str(jucator2.get()) == "foarfeca":
            rezultat.set(print("jucator1 căștigă"))
        elif str(jucator1.get()) == "piatră" and str(jucator2.get()) == "piatră":
            rezultat.set(print("egalitate"))

        elif str(jucator1.get()) == "hârtie" and str(jucator2.get()) == "hârtie":
            rezultat.set(print("egalitate"))
        elif str(jucator1.get()) == "hârtie" and str(jucator2.get()) == "foarfeca":
            rezultat.set(print("jucator2 căștigă"))
        elif jucator1.get() == "hârtie" and jucator2.get() == "piatră":
            rezultat.set(print("jucator1 căștigă"))

        elif jucator1.get() == "foarfecă" and jucator2.get() == "hârtie":
            print("jucator1 căștigă")
        elif jucator1.get() == "foarfecă" and jucator2.get() == "foarfeca":
            print("egalitate")
        elif jucator1.get() == "foarfecă" and jucator2.get() == "piatră":
            print("jucator2 căștigă")

        elif jucator1.get() != "foarfeca" "hârtie" "piatră" and jucator2.get() != "foarfeca" "hârtie" "piatră":
            print("""Ați greșit cuvântul sau o literă, vă rugam să încercați dinnou doar cu aceste 3 raspuns-uri:
                  foarfecă, hârtie sau piatră. """)

#-------------------------------------------------------#PARTEA 2----------------------------------------------------------------------------------

#generăm partea de tinker 
root = Tk()
root.config(bd=15)

jucator1 = StringVar()
jucator2 = StringVar()
rezultat = StringVar()

Label(root, text="jucator1").pack()
Entry(root,justify="center",textvariable=jucator1).pack()

Label(root, text="jucator2").pack()
Entry(root,justify="center",textvariable=jucator2).pack()

Label(root, text="rezultat").pack()
Entry(root,justify="center",textvariable=rezultat,state="disabled").pack()

Button(root, text="Click me",command=joc).pack(side="left")

root.mainloop()




#Acest proiect este clasicul joc piatră, hârtie și foarfecă, crearea este una simplă avem la început funcția care face ca jocul să
#funcționeze, apoi avem partea a doua în care reprezinta partea unu în Ui.