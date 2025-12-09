import feladat
import kiiras_helyzet
import jatekkezdes
import terkep
import ellenorzes
karakter_pozicio=0
map=["kerítésnél", "postaládánál", "bejáratnál", "konyhában", "hűtőnél", "lépcsőnél", "dolgozóban", "nappaliban", "laborban","börtönben"]



jateknak_vege=ellenorzes.vizsgalat(karakter_pozicio)
print(150*"*")
jatekkezdes.kezdes1()
print(150*"*")
jatekkezdes.kezdes2()
print(150*"*")
terkep.map()
print(150*"*")
jateknak_vege=ellenorzes.vizsgalat(karakter_pozicio)
print(150*"*")
while jateknak_vege==False:
    kiiras_helyzet.kiir(karakter_pozicio,map)
    print(150*"*")
    #ellenorzes.vizsgalat(karakter_pozicio)
    print(150*"*")
    karakter_pozicio=feladat.lepes(karakter_pozicio,map)
print(150*"*")
print("vége a játéknak")
