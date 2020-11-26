# binarni strom


def insert(tree, letter):
    if tree[0]:
        if ord(letter) < ord(tree[0]):
            if not tree[1]:
                tree[1] = [letter, None, None]
            else:
                insert(tree[1], letter)
        else:
            if not tree[2]:
                tree[2] = [letter, None, None]
            else:
                insert(tree[2], letter)
    else:
        tree[0] = letter
    return tree


# prazdny koren stromu - cislo, levy potomek, pravy potomek
tree = [None, None, None]  # tree[0], tree[1], tree[2]
for i in "ENGETO":
    insert(tree, i)

print(tree)

#VYSKA
def height(node):
    if node is None:
        return -1
    left_height = height(node[1])
    right_height = height(node[2])

    return 1 + max(left_height, right_height)

vyska = height(tree)
print(vyska)  # vyska stromu je 3

# HLOUBKA UZLU G
def get_level(letter, node, level):
    if node is None:
        return 0
    if letter in node:
        return level
    downlevel = get_level(letter, node[1], level + 1)
    if downlevel != 0:
        return downlevel
    downlevel = get_level(letter, node[2], level + 1)
    return downlevel

hloubka_pismena = get_level("G", node=tree, level=0)
print(hloubka_pismena)  # hloubka pro G ma byt 2


