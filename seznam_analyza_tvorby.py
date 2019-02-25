import copy

seznam = [0, 1, 2, 3, 4]
seznam.append(seznam)
print("seznam obsahujici sam sebe: ", seznam)
print(id(seznam[0]), id(seznam[5][0]))
# seznam obsahuje sam sebe, ale nemuze to vypsat bo by to delal donekonecna


# 1. takzvane kopirovani prirazenim
x = [6, 6, 6, 6]
y = x
y.append(50)
x.append(30)
y[1] = "f"
x[0] = "o"
print("kopirovani prirazenim\n{0} {1}".format(x, id(x)))  # obe promenne odkazuji na stejny objekt
print(y, id(y))


# 2. kopirovani slicem-velmi bezne
a = [4, 4, 4, 4, 4]
b = a[:]
b.append(7)
a.append(8)
b[0] = "b"
a[0] = "a"
print("kopirovani slicem")
print(a, id(a))
print(b, id(b))

# 2.a) pozor na problemy u slozenych listu
list1 = ["a", "b", ["ab", "ba"]]
list2 = list1[:]
print("slicing slozenych listu\n{} {}".format(list1, id(list1)))
print(list2, id(list2))
# bez problemu pro indexy 0 a 1
list2[0] = "c"
print("zmena bez side effectu\n{} {}".format(list1, id(list1)))
print(list2, id(list2))
# problem u podlistu
list2[2][0] = "d"
print("problem u podlistu")
print(list1, "id podlistu:", id(list1[2]))
print(list2, "id podlistu:", id(list2[2]))


# 3. metoda .copy() pro seznamy - chova se stejne jako slicing
e = [1, 1, 1, 1, [2, 2]]
f = e.copy()
e[0] = 0
f.append(20)
f[4][0] = 9
e[4][1] = 8
print("metoda copy pro seznamy")
print(e, id(e), "id podlistu", id(e[4]))
print(f, id(f), "id podlistu", id(f[4]))


# 4. fce copy() z modulu copy - chova se stejne jako slicing
c = [1, 2, 3, [4, 5], 6]
d = copy.copy(c)
c[0] = 10
d[0] = 15
c[3][0] = 900
d[3][1] = 800
print("fce copy z modulu copy")
print(c, id(c), "id podlistu", id(c[3]))
print(d, id(d), "id podlistu", id(d[3]))


s = "somestring"
u = s[:]
t = copy.copy(s)
# jedna se u vsech o stejny objekt, dokud se nezacne nejak modifikovat
print("kopirovani stringu")
print("puvodni s: ", s, id(s))
print("puvodni u: ", u, id(u))
print("puvodni t: ", t, id(t))
s = s[2:]
t = t[:3]
print("nove s: ", s, id(s))
print("nove u: ", u, id(u))
print("nove t: ", t, id(t))
"""
Rozdil mezi shallow a deep copy dava smysl jen u slozenych objektu, ktere obsahuji jine objekty, tj. seznamy, tridy...
"""


# 5. fce list - neni to bezne, ale je to platne; stejne omezeni jako vsechno vyse
k = [2, 2, 2, 2, [3, 3]]
m = list(k)
k.append(60)
m.append(40)
k[4][0] = 9
m[4][1] = 1000
print("fce list()")
print(k, id(k), id(k[4]))
print(m, id(m), id(m[4]))


# 6. metoda extend pro seznamy - stejne omezeni jako vsechno vyse
p = [3, 3, 3, 3, [8, 8]]
r = []
q = []
r.extend(p)
# q.append(p) tento seznam ma jen 1 prvek, a to cely seznam p jako podseznam
# print(q)
p[0] = 50
r[0] = 60
r[4][0] = 0
p[4][1] = 7
print("extend\n{} {} {}".format(p, id(p), id(p[4])))
print(r, id(r), id(r[4]))


# 7. fce deepcopy z modulu copy
g = [5, 5, 5, 5, ["a", "b"]]
h = copy.deepcopy(g)
print("deepcopy z modulu copy")
print(g,id(g), id(g[0]), id(g[4]), id(g[4][0]))
print(h, id(h), id(h[0]), id(h[4]), id(h[4][0]))
g[4][0] = "n"
h[4][0] = "c"
print(g, id(g), id(g[0]), id(g[4]), id(g[4][0]))
print(h, id(h), id(h[0]), id(h[4]), id(h[4][0]))
