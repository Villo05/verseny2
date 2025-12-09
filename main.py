import feladat
import kiiras_helyzet
import jatekkezdes
import terkep
import ellenorzes
karakter_pozicio=0
map=["kerítésnél", "postaládánál", "bejáratnál", "konyhában", "hűtőnél", "lépcsőnél", "dolgozóban", "nappaliban", "laborban", "erkélyen", "folyosón", "börtönben"]



jateknak_vege=ellenorzes.vizsgalat(karakter_pozicio)
print(150*"*")
jatekkezdes.kezdes1()
print(150*"*")
jatekkezdes.kezdes2()
print(150*"*")
terkep.map()
while jateknak_vege==False:
    jateknak_vege=ellenorzes.vizsgalat(karakter_pozicio)
    print(150*"*")
    kiiras_helyzet.kiir(karakter_pozicio,map)
    print(150*"*")
    ellenorzes.vizsgalat(karakter_pozicio)
    print(150*"*")
    feladat.lepes(karakter_pozicio,map)


