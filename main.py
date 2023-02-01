#megoldás
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    jszam: int = lapszamolas(jatekoslapok)
    gszam: int = lapszamolas(geplapok)
    if jszam > 21:
        print("játékos vesztett")
    if gszam > 21:
        print("gép vesztett")

def lapszamolas(lapok)->int:
    pontok: int = 0
    index: int = 0
    while index < len(lapok):
        pontok += lapok[index]
        index +=1
    return pontok


#teszteset



