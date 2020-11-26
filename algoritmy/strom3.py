def insert(tree, number):
    if tree[0]: # pokud uz strom ma koren
        if number < tree[0]: # vkladani mensiho cisla nez koren - vlevo
            if tree[1] is None: # je misto pro vlozeni
                tree[1] = [number, None, None]
            else: # pokud neni misto, pokracuje se do dalsi urovne
                insert(tree[1], number)
        else: # vkladani vetsiho cisla nez koren - vpravo
            if tree[2] is None: # je misto pro vlozeni
                tree[2] = [number, None, None]
            else: # pokud neni misto, pokracuje se do dalsi urovne
                insert(tree[2], number)
    else: # pokud koren jeste nema
        tree[0] = number


tree = [None, None, None]
insert(tree, 58)
insert(tree, 97)
insert(tree, 16)
insert(tree, 44)
insert(tree, 32)
insert(tree, 70)
insert(tree, 81)

print(tree)


def vyhledej(strom, prvek):
    prvek2 = None
    if strom is not None and strom != []:
        if strom[0] == prvek:
            prvek2 = prvek
        else:
            prvek2 = None
        prvek2 = vyhledej(strom[1], prvek)
        if prvek2:
            return prvek2
        else:
            prvek2 = vyhledej(strom[2], prvek)
        if prvek2:
            return prvek2
    return None

print(vyhledej(tree, 70))
