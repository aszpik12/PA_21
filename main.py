#megoldás
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    eredmenyek = ""
    jszam: int = lapszamolas(jatekoslapok)
    gszam: int = lapszamolas(geplapok)
    if jszam <= 21 and gszam<=21:
        if jszam > gszam:
            eredmenyek = ("a játékos nyert")
        elif gszam > jszam:
            eredmenyek = ("a gép nyert")
        elif gszam == jszam:
            if jszam < gszam:
                eredmenyek = ("a játékos nyert")
            elif jszam > gszam:
                eredmenyek = ("a gép nyert")
            else:
                eredmenyek = ("döntetlen")
    if jszam > 21:
        eredmenyek = "a játékos vesztett"
    if gszam > 21:
        eredmenyek = "a gép veszett"
    if jszam > 21 and gszam > 21:
        eredmenyek = "döntetlen mindkettő túl"

    return eredmenyek
def lapszamolas(lapok)->int:
    pontok: int = 0
    index: int = 0
    while index < len(lapok):
        pontok += lapok[index]
        index +=1
    return pontok

#teszteset

def jatekos_vesztett_teszt():
    jatekoskartyai = [10, 10, 10]
    gepkartyai = [2, 10, 7]
    print("játékos veszített teszt")
    vart: str = "a játékos vesztett"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")


def jatekos_nyert_kozelebb_teszt():
    jatekoskartyai = [2, 10, 8]
    gepkartyai = [5, 3, 5]
    gepkarty = lapszamolas(gepkartyai)
    jatkarty = lapszamolas(jatekoskartyai)
    print("játékos nyert közelebb teszt")
    vart: str = "a játékos nyert"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott and jatkarty>gepkarty:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")


def gep_nyert_kozelebb_teszt():
    jatekoskartyai = [2, 10, 2]
    gepkartyai = [2, 10, 7]
    gepkarty = lapszamolas(gepkartyai)
    jatkarty = lapszamolas(jatekoskartyai)
    print("gép nyert közelebb teszt")
    vart: str = "a gép nyert"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott and jatkarty<gepkarty:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")

def jatek_nyert_kozelebb_gep_tavolabb_teszt():
    jatekoskartyai = [3, 10, 2]
    gepkartyai = [8, 8, 8]
    gepkarty = lapszamolas(gepkartyai)
    jatkarty = lapszamolas(jatekoskartyai)
    print("jatek nyert kozelebb gep tavolabb teszt")
    vart: str = "a játékos nyert"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott and jatkarty < gepkarty and gepkarty > 21:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")

def jatek_vesztett_tavolabb_gep_kozelebb_teszt():
    jatekoskartyai = [2, 10, 2]
    gepkartyai = [5, 10, 1]
    gepkarty = lapszamolas(gepkartyai)
    jatkarty = lapszamolas(jatekoskartyai)
    print("kátékos vesztett tavolabb gep kozelebb teszt")
    vart: str = "a gép nyert"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott and gepkarty<jatkarty and jatkarty>21:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")

def jatekos_nyert_kevesebbkartyaval_teszt():
    jatekoskartyai = [2, 8, 10]
    gepkartyai = [8, 4, 4, 4]
    print("játékos vesztett több kártya teszt")
    vart: str = "döntetlen"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott and len(jatekoskartyai)<len(gepkartyai):
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")
def jatekos_vesztett_tobbkartyaval_teszt():
    jatekoskartyai = [2, 4, 6, 8]
    gepkartyai = [8, 8, 4]
    print("játékos vesztett több kártya teszt")
    vart: str = "döntetlen"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott and len(jatekoskartyai)>len(gepkartyai):
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")

def dontetlen():
    jatekoskartyai = [1, 7, 2]
    gepkartyai = [3, 5, 2]
    print("döntettlen teszt")
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    vart: str = "döntetlen"
    if kapott==vart:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")

def dontetlen_mindketto_tul():
    jatekoskartyai = [10, 6, 10]
    gepkartyai = [10, 10, 10]
    print("döntettlen mindketto túl teszt")
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    vart: str = "döntetlen mindkettő túl"
    if kapott==vart:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")

def gep_vesztett_teszt():
    jatekoskartyai = [2, 5, 10]
    gepkartyai = [10, 10, 10]
    print("gép veszített teszt")
    vart: str = "a gép veszett"
    kapott: str = eredmeny(jatekoskartyai, gepkartyai)
    if vart == kapott:
        print("teszt sikeres!")
    else:
        print("teszt sikertelen!")

def tesztek():
    jatek_nyert_kozelebb_gep_tavolabb_teszt()
    jatekos_nyert_kozelebb_teszt()
    jatekos_nyert_kevesebbkartyaval_teszt()
    jatek_vesztett_tavolabb_gep_kozelebb_teszt()
    jatekos_vesztett_teszt()
    jatekos_vesztett_tobbkartyaval_teszt()
    gep_nyert_kozelebb_teszt()
    gep_vesztett_teszt()
    dontetlen()
    dontetlen_mindketto_tul()

tesztek()

