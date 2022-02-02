
"""- Maak een crud systeem voor personeel.
- Elke personeelslid heeft een nummer, naam, functie en loon.
- Zorgt dat alle items aangepast, en verwijdert kunnen worden
- Functie loon_opslag personeel. Zorg dat je met een functie een procent of een vast bedrag kan toevoegen
- Voeg een key afdeling toe.
- Zorg dat je aan de hand van een key een filter kan toepassen per afdeling

-nog aan te passen: bij filteren de werknummer ook in de lijst=key"""

from tabulate import tabulate

pers = {
    1 : {
    "Naam" : "Jeanine Jans",
    "Functie": "CEO",
    "Loon": 3500,"Afdeling":"Kader"
    },
    2:{
    "Naam": "Albert Claes",
    "Functie": "Verkoper",
    "Loon": 2500,"Afdeling":"Verkoop"
    },
    3:{
    "Naam" : "Fons Segers",
    "Functie": "Aankoper",
    "Loon": 2000,"Afdeling":"Aankoop"
    }}

#Hoofd.druk het keuze menu af
def keuze_menu():
    print("1.Lijst personeel tonen")
    print("2.Personeel toevoegen")
    print("3.Personeel/item aanpassen")
    print("4.Personeel/item Verwijderen")
    print("5.Opslag (Opgelet !! Opslag moet je verdienen)")
    print("6.Filter per afdeling")

#1.Druk items af
def tonen(dictio):
    #for x,y in dictio.items():
    #    print(x,y)
    headers = ["Nummer", "Naam", "Functie", "Loon", "Afdeling"]
    dictio = [[name, *inner.values()] for name, inner in dictio.items()]
    print("")
    print(tabulate(dictio, headers=headers,tablefmt="grid"))
    print("")

#2.Voeg nieuwe werknemer toe
def toevoegen(dictio):
    nummer = len(dictio)+1
    naam = input("Geef de naam van de nieuwe werknemer " + str(nummer) + " in: ")
    functie = input("Geef de functie in: ")
    loon = input("Geef het loon in: ")
    afdeling = input("Geef de afdeling in: ")

    dictio[nummer] = {"Naam": naam ,"Functie": functie,"Loon": loon, "Afdeling": afdeling}
    tonen(dictio)
    return dictio
#3.Key en waarde aanpassen
def aanpassen(dictio):
    tonen(dictio)
    aan_te_passen_key=int(input("Geef het personeelsnummer waarvan u de aanpassing wil doen: "))
    if aan_te_passen_key in dictio:
        print(dictio[aan_te_passen_key])
        aan_te_passen_gen_key=input("Geef het item dat u wil aanpassen (Naam,Functie,Loon enz): ")
        if aan_te_passen_gen_key in dictio[aan_te_passen_key]:
            aan_te_passen_value=input("Geef de nieuwe waarde in: ")
            dictio[aan_te_passen_key][aan_te_passen_gen_key] = aan_te_passen_value
            tonen(dictio)
        else:
            print("Key staat niet in de lijst")
    else:
        print("Key staat niet in de lijst")
#4.verwijderd een item uit de lijst
def verwijder(dictio):
    tonen(dictio)
    nummer = int(input("Geef het personeelsnummer in dat u wilt verwijderen of waarvan u een item wil verwijderen: "))
    if nummer in dictio:
        bevestiging = input(print("Wil u de werknemer " + str(nummer) + " volledig verwijderen j/n ? "))
        if bevestiging == "j":
            dictio.pop(nummer)
            print(nummer," is weg uit de lijst")
        else:
            item=input("Geef het item dat u wil verwijderen uit " + str(nummer) + " : ")
            if item in dictio[nummer]:
                bevestiging2 = input("Bent u zeker dat u " + item + " bij " + str(nummer) + " wilt verwijderen j/n ? ")
                if bevestiging2 == "j":
                    dictio[nummer][item] = 0
                    print(item + " is verwijderd.")
            #elif item in dictio[nummer].values():
                #bevestiging2 = input("Bent u zeker dat u " + item + " van " + str(nummer) + " wilt verwijderen j/n ? ")
                #if bevestiging2 == "j":
                    #del dictio[nummer].(item)
                    #print(item + " als value verwijderen is niet mogelijk. Gebruik de functie aanpassen en zet de waarde op nul")
            else: print(item, " staat niet in de lijst")

    else:
        print(nummer, "is niet in de lijst")
    tonen(dictio)
#5.Opslag personeel
def opslag(dictio):
    tonen(dictio)
    nummer=int(input("Geef het nummer van de werknemer in : "))
    print("1. Opslag met een bedrag")
    print("2. Opslag met een percentage")
    keuze=input("Maak een keuze: ")
    if keuze=="1":
        bedrag=int(input("Met welk bedrag gaat het loon omhoog ? "))
        dictio[nummer]["Loon"] = dictio[nummer]["Loon"] + bedrag
    elif keuze=="2":
        procent=int(input("Met hoeveel procent gaat het loon omhoog ? "))
        dictio[nummer]["Loon"] = ((dictio[nummer]["Loon"] * procent)/100) + dictio[nummer]["Loon"]
    tonen(dictio)
#6. Aan de hand van een key een filter toepassen per afdeling
def filter_op(dictio):
    tonen(dictio)
    key = input("Op welke afdeling wil u filteren ? ")
    filter_dic = {}
    filter_rec = {}
    teller = 0
    for x in dictio.values():
        if (x["Afdeling"] == key):
            teller = teller + 1
            filter_rec.update({teller: {"Naam": x["Naam"],"Functie": x["Functie"], "Loon": x["Loon"], "Afdeling": x["Afdeling"]}})
            filter_dic.update(filter_rec)

    print((filter_dic.values()))

    kop={"Naam","Functie","Loon", "Afdeling"}
    print("")
    print(tabulate(filter_dic.values(), headers=filter_dic))
    print("")
#print(tabulate(dictio, headers=headers,tablefmt="grid"))

#hoofdprogramma
keuze_menu()
keuze = input("Wat wil je doen? Geef het nummer in of 'stop' om te stoppen ")
while(not keuze == "stop"):
    if(keuze == "1"):tonen(pers)
    elif(keuze == "2"):
        keuze = toevoegen(pers)
    elif(keuze == "3"):
        keuze = aanpassen(pers)
    elif(keuze == "4"):
        verwijder(pers)
    elif(keuze == "5"):
        opslag(pers)
    elif(keuze == "6"):
        filter_op(pers)
    keuze_menu()
    keuze = input("Maak een keuze 1-6 of 'stop' : ")
