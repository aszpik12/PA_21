#megoldás
def eredmeny(kartyaosszege):
    jszam = kartyaosszege[1]
    gszam = kartyaosszege[0]
    if jszam > 21:
        print("játékos vesztett")
    if gszam > 21:
        print("gép vesztett")

def lapszamolas(glist, jlist):
    gszamok=0
    index = 0
    while index < len(glist):
        gszamok += glist[index]
        index +=1

    jszamok=0
    index = 0
    while index < len(jlist):
        jszamok += jlist[index]
        index +=1
    kartyakosszege = [gszamok, jszamok]
    return kartyakosszege

glist = [5, 3, 5, 3, 7, 2]
jlist = [7, 4, 2, 5, 2]
lapszamolas(glist, jlist)
eredmeny(lapszamolas())

#teszteset



