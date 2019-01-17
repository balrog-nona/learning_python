"""
Bajt je trida.
Object typu bajt definovany pomoci b; uvnitr bajtoveho literalu muze byt ASCII znak nebo zakodovane sestnactokove
cislo od \x00 do \xff (tj. 0-255).
Polozkami objektu typu bytes jsou cisla 0-255.
Objekt typu bytes je nemenitelny, jednotlivym bajtum nelze nic priradit (stejne jako stringum). Pri potrebe zmeny
jednotliveho bajtu je treba pouzit slicing a konkatenaci nebo konvertovat objekt na bytearray.
"""

by = b'abcd\x65'  # zde e vysledkem sestnactkoveho cisla
print(by)
print(type(by))

print(len(by))

by += b'\xff'  # funguje konkatenace
print(by)
print(len(by))
print(by[0])  # polozkami objektu jsou cisla
print(by[5])
# by[0] = 102 vyvola TypeError

by = b'abcd\x65'
barr = bytearray(by)  # vsechny operace, ktere se daji delat s byte funguji i s bytearray
print(barr)
print(len(barr))
barr[0] = 102  # lze priradit hodnotu jednotlivemu bajtu cislem 0-255
print(barr)

"""
Nelze michat bajty a retezce:
by = b'd
s = 'abcde'
print(by + s) vyvola TypeError; neze je spojovat bo to jsou ruzne datove typy
Python 3 neprovadi implicitni konverzi bajtu na retezce a naopak - pouzit metodu decode() z tridy bajt nebo
encode() z tridy string! Kodovani existuje cela rada, napr. ascii, utf-8, gb18030, big5...
"""

by = b'd'
s = 'abcd'
# s.count(by) tohle nefunguje - v retezci zadne bajty nejsou!
pocet = s.count(by.decode('ascii'))  # konverze se musi vyslovne vyjadrit - metoda decode()
print(pocet)
