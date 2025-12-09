import feladat
import kiiras_helyzet
import jatekkezdes
import terkep
import ellenorzes
karakter_pozicio=0
map=["kerítésnél", "postaládánál", "bejáratnál", "konyhában", "hűtőnél", "lépcsőnél", "dolgozóban", "nappaliban", "laborban","börtönben"]


RED = "\033[91m"
BOLD = "\033[1m"

print(RED + BOLD)
jateknak_vege=ellenorzes.vizsgalat(karakter_pozicio)

print("▓" * 100)
jatekkezdes.kezdes1()
print("▓" * 100)
jatekkezdes.kezdes2()
print("▓" * 100)
terkep.map()
print("▓" * 100)
while jateknak_vege==False:
    kiiras_helyzet.kiir(karakter_pozicio,map)
    print("▓" * 100)
    karakter_pozicio=feladat.lepes(karakter_pozicio,map)
    print("▓" * 100)    #ellenorzes.vizsgalat(karakter_pozicio)
    jateknak_vege=ellenorzes.vizsgalat(karakter_pozicio)
jatekkezdes.befejezes()
