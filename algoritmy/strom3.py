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

print("strom original:\n", tree)

def search(tree, number):
    if tree is None:
        return None
    elif number < tree[0]:
        return search(tree[1], number)
    elif number > tree[0]:
        return search(tree[2], number)
    else:
        return number


#print(search(tree, 81))
#print(search(tree, 1000))


# MAZANI
def delete(tree, number):
    if tree is None:
        return None
    elif tree[0]:
        if number < tree[0]:
            delete(tree[1], number)         # Nejedná se o hledané číslo.
        elif number == tree[0] and tree[1] is None and tree[2] is not None:     # Má jen levého potomka.
            tree[0] = tree[2][0]
            tree[1] = tree[2][1]
            tree[2] = tree[2][2]
        elif number == tree[0] and tree[1] is not None and tree[2] is None:     # Má jen pravého potomka.
            tree[0] = tree[1][0]
            tree[2] = tree[1][2]
            tree[1] = tree[1][1]    # Nesmíme přijít o následníky, proto ukládáme tuto část jako poslední.
        else:
            delete(tree[2], number)


#delete(tree, 70)


def delete_cv(tree, number):
    if tree is None:
        return None
    elif tree[0]:
        if number < tree[0]:
            if tree[1] == [number, None, None]:
                tree[1] = None
            else:
                delete_cv(tree[1], number)
        elif tree[0] == [number, None, None]:
            tree.clear()
        else:
            if tree[2] == [number, None, None]:
                tree[2] = None
            else:
                delete_cv(tree[2], number)


delete_cv(tree, 81)
print(tree)
delete_cv(tree, 1)
print(tree)
delete_cv(tree, 58)
print(tree)
