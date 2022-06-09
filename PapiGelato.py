import tkinter
from tkinter import messagebox
from tkinter import ttk
import threading
from tkinter import font
import yaml
from yaml.loader import SafeLoader

##### ReadValues #####
with open('settings.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

##### values #####
smakenLijst = data['smaken']
toppingLijst = data["toppingList"]
prijsPerLiter = data["liter"]
prijsPerBolletje = data["bolletjes"]
totalScoops = 0

##### functions #####

def toppings():
    global toppingWindow
    try:
        window.withdraw()
        toppingWindow.deiconify()
    except:
        window.withdraw()
        toppingWindow = tkinter.Tk()
        tkinter.Label(toppingWindow,text="welke topping wil je?").pack()
        amountOfRadiobuttons1 = 0
        gekozenTopping = tkinter.StringVar()
        for i in range(len(toppingLijst)):
            if amountOfRadiobuttons1 > 4:
                amountOfRadiobuttons1 = 0
            exec(f"choise{i} = ttk.Radiobutton(toppingWindow,text='{toppingLijst[i]}',variable=gekozenTopping,value='{toppingLijst[i]}')")
            exec(f"choise{i}.pack()")
            amountOfRadiobuttons1 += 1
        continueButton = tkinter.Button(toppingWindow,text="Continue",command=particulierBonnetje)
        continueButton.pack()
        toppingWindow.mainloop()

def updateExampleText(*args):
    exampleText.config(font=("Comic_Sans",textSizeValue.get()))

def bonnetjeZakelijk():
    window.withdraw()
    bonnetjeWindow = tkinter.Tk()
    tkinter.Label(bonnetjeWindow,text="-----Papi gelato-----", font=("Comic_Sans",textSizeValue.get())).pack()
    tkinter.Label(bonnetjeWindow,text=f"""
    {liter.get()} Liter        =       €{float(prijsPerLiter) * float(liter.get())}

    -------------------------------------------------------------------------------
    TotaalPrijs         =       €{float(prijsPerLiter) * float(liter.get())}
    """,font=("Comic_Sans",textSizeValue.get())).pack()
    bonnetjeWindow.mainloop()

def settings():
    global textSizeValue
    global exampleText
    global continueButton
    settingsWindow = tkinter.Tk()
    textSizeValue = tkinter.IntVar(value=20)
    exampleText = tkinter.Label(settingsWindow,text="Example",font=("Comic_Sans",textSizeValue.get()))
    exampleText.grid(column=1,row=1)
    textSize = ttk.Scale(settingsWindow,from_=1,to=50,orient="horizontal",variable=textSizeValue,length=200)
    textSize.grid(column=1,row=3)
    textSize.grid(columnspan=2)
    textSizeValue.trace("w",updateExampleText)
    continueButton = tkinter.Button(text = "continue",command=settingsWindow.destroy,bg="green",font=("Comic_Sans",textSizeValue.get()))
    continueButton.grid(column=1,row=4)
    settingsWindow.mainloop()

def editTextZakelijkSmaken():
    global choosingLiter
    choosingLiter += 1
    if choosingLiter == int(liter.get()):
        bonnetjeZakelijk()
    else:
        textVar.set(f"What taste do you want for Liter {choosingLiter + 1}")

def smakenZakelijk():
    global choosingLiter
    try:
        liters = int(liter.get())
        amountOfRadiobuttons = 0
        choosingLiter = 0
        textVar.set(f"What taste do you want for Liter {choosingLiter + 1}")
        whatRow = 1
        whatColumn = 0
        continueButton2.destroy()
        gekozenSmaak = tkinter.StringVar()
        howMuchLiter.destroy()
        for i in range(len(smakenLijst)):
            if amountOfRadiobuttons > 4:
                amountOfRadiobuttons = 0
                whatRow += 1
                whatColumn = 0
            exec(f"choise{i} = ttk.Radiobutton(text='{smakenLijst[i]}',variable=gekozenSmaak,value='{smakenLijst[i]}')")
            exec(f"choise{i}.grid(column={whatColumn},row={whatRow})")
            amountOfRadiobuttons+= 1
            whatColumn += 1
        nextButton = tkinter.Button(text="Next",command=editTextZakelijkSmaken)
        nextButton.grid(column=2,row=whatRow + 1)

    except:
        messagebox.showerror(message="Something went wrong...\nare you sure you entered everything correctly?")

def particulierBonnetje(*args):
    global totalScoops
    toppingWindow.withdraw()
    totalScoops += int(howManyScoops.get())
    if messagebox.askyesno(message="Do you want to order more?"):
        window.withdraw()
        zakelijkOfParticulierCheck()
        RadioButtons.destroy()
        window.deiconify()
    else:
        window.destroy()
        bonnetje = tkinter.Tk()
        tkinter.Label(text=f"""
        ------------- Papi Gelato -------------

        Bolletjes {totalScoops} = €{round(float(totalScoops) * float(prijsPerBolletje),2)}

        total = €{round(float(totalScoops) * float(prijsPerBolletje),2)}
        """).pack()
        bonnetje.mainloop()


def editTextParticulier():
    global choosingBolletje
    choosingBolletje += 1
    if choosingBolletje == int(howManyScoops.get()):
        window.withdraw()
        toppings()
        
    else:
        textVar.set(f"What taste do you want your scoop nr {choosingBolletje + 1}?")

def welkeSmaakParticulier():
    try:
        global RadioButtons
        int(howManyScoops.get())
        gekozenSmaak = tkinter.StringVar()
        global choosingBolletje
        scoops.destroy()
        choosingBolletje = 0
        amountOfRadiobuttons = 0
        continueButton3.destroy()
        textVar.set(f"What taste do you want your scoop nr {choosingBolletje + 1}?")
        whatRow = 1
        whatColumn = 0

        RadioButtons = tkinter.LabelFrame()
        RadioButtons.grid(column=0,row=2)
        for i in range(len(smakenLijst)):
            if amountOfRadiobuttons > 4:
                amountOfRadiobuttons = 0
                whatRow += 1
                whatColumn = 0
            exec(f"choise{i} = ttk.Radiobutton(RadioButtons,text='{smakenLijst[i]}',variable=gekozenSmaak,value='{smakenLijst[i]}')")
            exec(f"choise{i}.grid(column={whatColumn},row={whatRow})")
            amountOfRadiobuttons+= 1
            whatColumn += 1
        nextButton = tkinter.Button(RadioButtons,text="Next",font=("Comic_Sans",textSizeValue.get()),command=editTextParticulier)
        nextButton.grid(column=2,row=whatRow + 1)
    except Exception as e:
        print(e)
        messagebox.showerror(message="an error ocurred...\nare you sure you entered everything correctly?")

def zakelijkOfParticulierCheck(*args):
    global liter
    global scoops
    global textLabel
    global textVar
    global howMuchLiter
    global continueButton2
    global continueButton3
    global howManyScoops
    try:
        particulier.destroy()
        zakelijk.destroy()
    except:
        pass

    # ##### Create settings button #####     (I don't know how to make the labels update live without crashing the program.)
    # settingsButton = tkinter.Button(text="Settings",bg="green",command=settings,font=("Comic_Sans",textSizeValue.get()))
    # settingsButton.grid(column=3,row=5)

    ##### Create Label for text #####
    textVar = tkinter.StringVar(value="Default Text")
    textLabel = tkinter.Label(textvariable=textVar, font=("Comic_Sans",textSizeValue.get()))
    textLabel.grid(columnspan=5)
    textLabel.grid(column=0,row=0)

    # ##### Start threading timer #####
    # threading.Timer(1,callUpdateLabels).start()
    
    ##### gaat naar particulier of zakelijk #####
    if partOfZak.get() == "b":
        textVar.set("How much Liter of icecream do you want?")
        liter = tkinter.IntVar()
        howMuchLiter = tkinter.Entry(textvariable=liter,font=("Comic_Sans",textSizeValue.get()))
        howMuchLiter.grid(column=2,row=2)
        continueButton2 = tkinter.Button(text="Continue",command=smakenZakelijk)
        continueButton2.grid(column=2,row=3)

    elif partOfZak.get() == "p":
        textVar.set("How many icecream scoops do you want?")
        howManyScoops = tkinter.IntVar()
        scoops = tkinter.Entry(textvariable=howManyScoops,font=("Comic_Sans",textSizeValue.get()))
        scoops.grid(column=0,row=2)
        continueButton3 = tkinter.Button(text="Continue",font=("Comic_Sans",textSizeValue.get()),bg="green",command=welkeSmaakParticulier)
        continueButton3.grid(column=0,row=3)
    else:
        messagebox.showerror(message="idk what you did, but you broke it.")

settings()

window = tkinter.Tk()

##### kies particulier/zakelijk #####
partOfZak = tkinter.StringVar()
zakelijk = ttk.Radiobutton(window,variable=partOfZak,value="b",text="for Business")
particulier = ttk.Radiobutton(window,variable=partOfZak,value="p",text="private")
zakelijk.pack()
particulier.pack()
partOfZak.trace("w",zakelijkOfParticulierCheck)

window.mainloop()


##### Einde window 1 #####
























######### oude code #########

aantal = 0
herhalen = "y"
repeat = True
TotaalBakjes = 0
totaalHoorntjes = 0
TotaleBolletjes = 0
particulier = "...."

#------Zakelijk------#
Liters_ijs = 0
Btw = 6
prijsPerLiter = 9.80
#-----------------------#

Besteldesmakenlijst = []
BestaandeSmaken = ["aardbei", "a", "chocolade", "c", "vanille", "v"]

toppings = []
aantalToppings = 0
bestaandeToppings = ["sl", "slagroom", "sp", "sprinkels", "c", "caramel"]
toppingKosten = 0.00

prijsPerBakje = 0.75
prijsPerHoorntje = 1.25
prijsPerBolletje = 0.95

print("Welkom bij Papi Gelato.")

def WrongAnswer():
    print("Sorry dat is geen optie die we aanbieden...")

def AantalLiter():
    global Liters_ijs
    Liters_ijs = int(input("Hoeveel liter ijs wilt U bestellen?: "))

def topping():
    
    
        toppingKeuze = input("Wat voor topping wilt u: (G) Geen, (Sl) Slagroom, (Sp) Sprinkels of (C) Caramel Saus?: ").lower()
        if toppingKeuze == "g":
            print("")
            
        elif toppingKeuze in bestaandeToppings:
            
            toppings.append(toppingKeuze)
            global aantalToppings
            global toppingKosten
            aantalToppings += 1

            if toppingKeuze == "sl" or "slagroom":
                
                toppingKosten += 0.50
            elif toppingKeuze == "sp" or "sprinkels":
                
                toppingKosten += (0.30 * aantal)
            elif toppingKeuze == "c" or "caramel":
                if bakjeOfHoorntje == "bakje":
                    
                    toppingKosten += 0.90
                elif bakjeOfHoorntje == "hoorntje":
            
                    toppingKosten += 0.60

        else:
            WrongAnswer()

def ParticulierSmaak():
    print("Welke smaak wilt u hebben?")
    print("Aardbei(A), Chocolade(C) of Vanille(V)")
    smaak = input("Welke smaak ijs wilt U?")


def smaak():
    print("Welke smaak wilt u hebben?")
    print("Aardbei(A), Chocolade(C) of Vanille(V)")
    returnsInLoop = 1
    while returnsInLoop != aantal + 1:
        smaak = input("Welke smaak wilt U hebben voor uw "+ str(returnsInLoop) + "e bolletje?").lower()
        if smaak in BestaandeSmaken:
            returnsInLoop += 1
            Besteldesmakenlijst.append(smaak)
            
        else:
            WrongAnswer()


def aantalbolletjes():
    repeater = "enabled"
    while repeater == "enabled":
        aantalBolletjesijs = int(input("Hoe veel bolletjes ijs wil je?: "))
        if aantal > 0:
            repeater = "disabled"
            return aantalBolletjesijs
        else:
            WrongAnswer()

def WatVoorVerpakking():
    if aantal <= 3:
        waarin = keuzeBakjeOfHoorntje()

    elif aantal > 3 and aantal < 8:
        print("Dan krijgt u van mij een bakje met", aantal, "bolletjes.")
        waarin = "bakje"
    
    elif aantal > 8:
        print("Sorry, maar zulke grote bakjes hebben wij niet.")
        waarin = "ERROR"
    
    else:
        WrongAnswer()
        waarin = "ERROR"
    
    return waarin

def keuzeBakjeOfHoorntje():
    soort = input("Wilt U een hoorntje of een bakje?(H of B): ").lower()
    if soort == "b":
        soort = "bakje"
    elif soort == "h":
        soort = "hoorntje"
    return soort

def nogEenKeer():
    smaak()
    topping()
    print("Hier is uw", bakjeOfHoorntje, "met", aantal, "bolletje(s)")
    overnieuw = input("Wilt u nog wat bestellen?(Y/N): ").lower()
    return overnieuw

while repeat == True:
    Soort = input("Bent u Particulier (P) of zakelijk (Z)?: ").lower()
    if Soort == "p" or Soort == "particulier":
        herhalen = "y"
        particulier = "ja"
        repeat = False
    elif Soort == "z" or Soort =="zakelijk":
        particulier = "nee"
        herhalen = "n"
        repeat = False
    else:
        WrongAnswer()
        repeat = True


while herhalen == "y":
    def Particulier():
        global aantal
        global herhalen
        global TotaleBolletjes
        global totaalHoorntjes
        global TotaalBakjes
        global bakjeOfHoorntje
        aantal = aantalbolletjes()

        bakjeOfHoorntje = WatVoorVerpakking()
        if bakjeOfHoorntje != "ERROR":
            herhalen = nogEenKeer()
            TotaleBolletjes += aantal
            if bakjeOfHoorntje == "bakje":
                
                TotaalBakjes = TotaalBakjes + 1
            elif bakjeOfHoorntje == "hoorntje":
                totaalHoorntjes = totaalHoorntjes + 1
            else:
                WrongAnswer()
        else:

            print("")
    particulier()

if particulier == "nee":
    Litersijs = AantalLiter()
    ParticulierSmaak()

if particulier == "ja":
    print('---------["Papi Gelato"]---------')
    print("")
    if TotaleBolletjes >= 1:
        print("Bolletje(s)    "+ str(TotaleBolletjes)+ " X " + "€" + str(round(float(TotaleBolletjes) * prijsPerBolletje,2)))

    if totaalHoorntjes >= 1:
        print("Hoorntje(s)    "+ str(totaalHoorntjes)+ " X " + "€" + str(round(float(totaalHoorntjes) * prijsPerHoorntje,2)))

    if TotaalBakjes >= 1:
        print("Bakje(s)       "+ str(TotaalBakjes)+ " X " + "€" + str(round(float(TotaalBakjes) * prijsPerBakje,2)))

    if aantalToppings >= 1:
        print("topping(s)     "+ str(aantalToppings)+ " X " + "€" + str(round(toppingKosten,2)))

    print("                   ----- +")
    totaalprijs = float(totaalHoorntjes) * prijsPerHoorntje + float(TotaalBakjes) * prijsPerBakje + TotaleBolletjes * prijsPerBolletje
    totaal2 = round(float(totaalprijs),2)

    print("Totaal"+ "              "+ "€" + str(totaal2))
else:
    print('---------["Papi Gelato"]---------')
    print("")
    totaalprijs = float(Liters_ijs) * float(prijsPerLiter)
    totaalprijs2 = round(float(totaalprijs),2)
    print("Liter   "+ str(Liters_ijs), " X "+ str(prijsPerLiter)+ " = "+"€"+ str(totaalprijs2))
    print("                -------- +")
    btwprijs = round(float(totaalprijs/100 * Btw),2)
    print("Totaal           = €"+ str(totaalprijs2))
    print(f'BTW               {round(totaalprijs2 / 106 * Btw, 2)}€')

