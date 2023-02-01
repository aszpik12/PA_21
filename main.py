#megoldás
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    jszam: int = lapszamolas(jatekoslapok)
    gszam: int = lapszamolas(geplapok)
    if jszam > 21:
        eredmenyek = "a játékos vesztett"
        return eredmenyek
    if gszam > 21:
        eredmenyek = "a gép veszett"
        return eredmenyek

def lapszamolas(lapok)->int:
    pontok: int = 0
    index: int = 0
    while index < len(lapok):
        pontok += lapok[index]
        index +=1
    return pontok

#teszteset



