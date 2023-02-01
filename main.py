#megoldás
def eredmeny(gszam, jszam):
    if jszam > 21:
        print("játékos vesztett")
    if gszam > 21:
        print("gép vesztett")
#teszteset
eredmeny(21, 25)


