def lepes(karakter_pozicio,map):
    
    if karakter_pozicio==0:
        lepesadat=""
        while lepesadat!="j":
            lepesadat=input(f"merre szeretnél menni?jobbra=j: ")
            karakter_pozicio+=1
    else:
        lepesadat=input("merre szeretnél menni?jobbra=j,balra=b: ")
    if lepesadat=="j":
        karakter_pozicio+=1
        print(f"jelenleg a {map[karakter_pozicio]} vagy")
    else:
        karakter_pozicio-=1
        print(f"jelenleg a {map[karakter_pozicio]} vagy")
    return karakter_pozicio

