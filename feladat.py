import terkep
import jatekosok

def karakter_valasztas ():
    valasz=True
    while valasz==True:
        valasztas=input("Válassz egy karaktert( Albert, Cecíl, Béla): ")
        if valasztas=="Albert" or valasztas=="a" or valasztas=="A" or valasztas=="albert" or valasztas=="Béla" or valasztas=="b" or valasztas=="B" or valasztas=="bela" or valasztas=="Cecíl" or valasztas=="c" or valasztas=="C" or valasztas=="cecil":
            if valasztas=="Albert"or"a"or"A"or"albert":
                print("Albertet választottad")
                valasz=False
                kivalasztott_karakter="Albert"
            elif valasztas=="Béla"or"b"or"B"or"bela":
                print("Bélát választottad")
                valasz=False
                kivalasztott_karakter="Béla"
            else:
                print("Cecílt választottad")
                kivalasztott_karakter="Cecíl"
                valasz=False
        else:
            print("Nincs ilyen karakter, próbáld újra!")
        
    return kivalasztott_karakter

def lepes(kivalasztott_karakter,a_pozicio,b_pozicio,c_pozicio):
    if kivalasztott_karakter=="Albert":
        pozicio=a_pozicio
    elif kivalasztott_karakter=="Béla":
        pozicio=b_pozicio
    else:
        pozicio=c_pozicio
    if pozicio==0:
        lepes=input(f"Merre menjen {kivalasztott_karakter} (jobbra='j'): ")
    else:
        lepes=input(f"Merre menjen {kivalasztott_karakter} (jobbra='j',balra='b'): ")
    if kivalasztott_karakter=="Albert":
        if lepes=="j":
            a_pozicio+=1
        else:
            a_pozicio-=1
    elif kivalasztott_karakter=="Béla":
        if lepes=="j":
            b_pozicio+=1
        else:
            b_pozicio-=1
    else:
        if lepes=="j":
            c_pozicio+=1
        else:
            c_pozicio-=1
    print(f"{kivalasztott_karakter} most a {terkep.terkep()[pozicio]} .")


lepes(karakter_valasztas(),jatekosok.albert(),jatekosok.bela(),jatekosok.cecil())