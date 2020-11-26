# z Engeto - binarni strom
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

# prazdny koren stromu - cislo, levy potomek, pravy potomek
tree = [None, None, None]
insert(tree, 25)
insert(tree, 14)
insert(tree, 37)
insert(tree, 19)
insert(tree, 42)
insert(tree, 70)
insert(tree, 3)
insert(tree, 56)
insert(tree, 61)
insert(tree, 83)

print(tree)
print(type(tree))

# VYSKA STROMU
def high_rec(tree):  # pomoci rekurze
    if tree != None and tree != []: # Ošetření konce stromu a prázdného pole.
        if tree[0] == None: # Ošetření jen inicializovaného stromu.
            return 0
        left_high = high_rec(tree[1])
        right_high = high_rec(tree[2])
        if left_high > right_high: # Bereme vždy doposud větší dosaženou výšku.
            return left_high + 1
        else:
            return right_high + 1
    else:
        return 0 # Potomky listových uzlů.

print("vyska rekurzivne", high_rec(tree))


def high_non_rec(tree):  # iteracni reseni
    q = []
    q.append(tree)
    high = 0
    if tree != [None, None, None] and tree != []:
      while q: # Dokud budeme mít co procházet – dokud naše pole pro procházení do šířky nebude prázdné.
          high = high + 1 # Výška v dané úrovni.
          node_count = len(q) # Počet uzlů v dané úrovni.
          for i in range(0, node_count): # Zpracování všech uzlů dané úrovně a jejich podstromů.
            subtree = q[0]
            q.pop(0)
            if subtree[1] != None:
              q.append(subtree[1])
            if subtree[2] != None:
                q.append(subtree[2])
      return high
    else:
      return 0

print("vyska iteracne", high_non_rec(tree))

# POCET UZLU
# rekurzivne
def node_count_rec(tree, count):
    if tree != None and tree != []:
        if tree[0] == None:
            return 0
        count = node_count_rec(tree[1], count)
        count = node_count_rec(tree[2], count)
        return count + 1
    else:
        return count

print("uzly rekurzivne", node_count_rec(tree, 0))

# iteracne
def node_count_iter(tree):
    q = []
    q.append(tree)
    nodes = 1
    if tree != [None, None, None] and tree != []:
        while q:  # Dokud budeme mít co procházet – dokud naše pole pro procházení do šířky nebude prázdné.
            for i in range(0, len(q)):  # Zpracování všech uzlů dané úrovně a jejich podstromů.
                subtree = q[0]
                q.pop(0)
                if subtree[1] != None:
                    nodes += 1
                    q.append(subtree[1])
                if subtree[2] != None:
                    nodes += 1
                    q.append(subtree[2])
        return nodes
    else:
        return 0

uzly = node_count_iter(tree)
print("uzly iteracne", uzly)

#VYVAZENOST STROMU
def balance(tree):

    if tree is None: # Prázdny strom je vyvážený.
        return True

    left_high = high_rec(tree[1]) # Zjistíme výšku levého a pravého podstromu.
    right_high = high_rec(tree[2])
    # Kontrola, zda se výšky liší maximálně o 1.
    if (abs(left_high - right_high) <= 1) and balance(tree[1]) is True and balance(tree[2]) is True:
        return True
    return False# Není splněna podmínka.

print(balance(tree))  # je nevyvazeny


def inorder(tree, array):
    if tree is None:
        return
    inorder(tree[1], array)
    array.append(tree)
    inorder(tree[2], array)

def array_to_tree(array):
    if array == []:
        return None
    median_pos = len(array) // 2         # Sečte pozici mediánu v poli.
    new_tree = [array[median_pos], None, None]          # Nastaví medián jako kořen.
    new_tree[1] = array_to_tree(array[:median_pos])     # Medián levé poloviny nastavený jako levý potomek.
    new_tree[2] = array_to_tree(array[median_pos + 1:]) # Medián pravé poloviny nastavený jako pravý potomek.
    return new_tree

