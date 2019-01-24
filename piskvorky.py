#tah hráče

def tah_hrace(pole):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    while True:
        cislo_policka = int(input("Kam chceš hrát? "))
        if cislo_policka < 0:
            print("Záporné čísla nejde zadávat")
        elif cislo_policka > 19:
            print("Čísla musí být menší než 19")
        elif pole[cislo_policka] != "-":
            print("Toto políčko je již obsazeno, zadej jiné")
        else:
            return (pole[:cislo_policka] + "o" + pole[cislo_policka+1:])
            break


#tah počítače
def tah_pocitace(pole):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    from random import randrange
    if "x-" in pole:
        return pole.replace("x-","xx")
    elif "-x" in pole:
        return pole.replace("-x","xx")
    elif "o-" in pole:
        return pole.replace("o-","ox")
    elif "-o" in pole:
        return pole.replace("-o","xo")
    else:
        while True:
            cislo_policka = randrange(0,20)
            if cislo_policka == "-":
                return (pole[:cislo_policka] + "x" + pole[cislo_policka+1:])
    
#vyhodnot funkce
def vyhodnot (pole):
    if "xxx" in pole:
        return("Bohužel, vyhrál hráč počítač.") 
    elif "ooo" in pole:
        return("Gratuluji k výhře!")
    elif "-" not in pole and "xxx" not in pole and "ooo" not in pole:
        return("Remíza")
    else:
        return("-")


#piskvorky 1D
def piskvorky_1D():
    pole = "--------------------"
    pokracovani = True
    while pokracovani:
        pole = tah_hrace(pole)
        print(pole)
        pokracovani = vyhodnot(pole)
        if pokracovani == "-":
            pokracovani = True
        else:
            print(pokracovani)
            pokracovani = False
            break
        pole = tah_pocitace(pole)
        print(pole)
        pokracovani = vyhodnot(pole)
        if pokracovani == "-":
            pokracovani = True
        else:
            print(pokracovani)
            pokracovani = False
            break

piskvorky_1D()







