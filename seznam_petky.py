seznam = [5, 5, 5, 5, 5]
seznam2 = [[5, 5, 5, 5, 5]]
seznam3 = seznam + seznam2
print(seznam3, len(seznam3))

seznam3[-1] = seznam3[-1][-1] * 6
print(seznam3)

"""
seznam = list(range(5, 6)) * 6 # da [5, 5, 5, 5, 5, 5]
i = 5

seznam[i] = list(range(5, 6)) * 6
seznam[i][i] = list(range(5, 6)) * 6

posledni_prvek = [5, 5, 5, 5, 5, 5]

while x >= 0:
    

print(seznam)
"""
