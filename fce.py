def filter(fce, seznam):
    seznam2 = []
    for i in seznam:
        if fce(i) == True:
            seznam2.append(i)
    return seznam2


"""
generator - kdyz ma fce vracet pole/iterable
yield vi, ze navratova vec bude list a pokazde, kdyz se narazi na yield tak prida do neho polozku
mene narocne na pamet, dokaze tvorit polozky az jednu po druhe, ne hned vsechny naraz
"""

def filter(fce, seznam):
    for i in seznam:
        if fce(i):
            yield i  # precit dokumentaci, zde pak nelze pouzit return
