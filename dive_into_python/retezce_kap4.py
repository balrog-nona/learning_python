import humansize
import sys

"""
O znakovem kodovani se da uvazovat jako o desifrovacim klici - kazde kodovani muze pro stejny znak pouzivat jinou
posloupnost bajtu. K dekodovani jakohokoli textu (souboru, webove stranky...) je treba vedet to, jake kodovani
bylo pouzito. Prevadi cisla srozumitelna pocitaci na znaky citelne cloveku.

Anglictina a zapadoevropske jazyky se vlezou s kodovanim do 1 bajtu(tj. nejvetsi mozne cislo je 255.

UNICODE - vyjadruje kazdy znak z kazdeho jazyka; kazde pismeno/znak/ideogram se vyjadruje jako 4bajtove cislo. Kazde
cislo vyjadruje jedinecny znak pouzivany aspon v 1 jazyce sveta (pouzitych znaku je kolem 65 535).
Nicmene takovy pristup je narocny na pamet, protoze 4 bajty na nazdy jeden znak je hodne.
UTF-32 pouziva 4 bajty (32 bitu) na znak
UTF-16 pouziva 2 bajty, znaky z intervalu 0 - 65535 se koduji do dvou bajtu
UTF-8 - kodovani s promennou delkou, tj. ruzne Unicode znaky zabiraji ruzny pocet bajtu, tj. ASCII znaky jen 1 bajt na
znak, znaky z rozsirene latinky zabiraji2 bajty, cinske znaky 3 bajty...

V Pythonu 3 jsou vsechny retezce posloupnosti znaku v Unicode
"""

# compound file names
si_siffixes = humansize.SUFFIXES[1000]  # 1000 je klic, hodnota je seznam
print(si_siffixes)
print('1000{0[0]} = 1{0[1]}'.format(si_siffixes))  # nahrazovani za hodnoty ze seznamu: 0[0] prvni prvek, 0[1] druhy
"""
Dalsi metody:
- predani slovniku a zpristupneni hodnoty klicem
- predani modulu a zpristupneni promennych a fci jmenem
- predani instance tridy a zpristupneni jejich vlastnosti a metod jmenem
- kombinace vyse uvedeneho
"""
# pro inspiraci
print('1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys))
"""
Jak to funguje:
- modul sys v sobe udrzuje info o momentalne bezici pythonovske instanci. Modul sys byl importovan,takze ho jde predat
jako argument metody format
- sys.modules je slovnik vsech modulu, ktere byly importovany toutoinstanci Pythonu. Klicem je jmeno modulu, hodnotou
je objekt modulu, tj. 0.modules odkazuje na slovnik importovanych modulu
- uvnitr oblasti nahrad jde vynechat apostrofy kolem klice humansize, normalne v kodu je to totiz 
sys.modules['humansize']. K tomu PEP 3101
- sys.modules[humansize].SUFFIXES je promenna z modulu humansize
- SUFFIXES[1000][0] je pouziti klice a pak odkaz na prvni polozku seznamu 
"""

# specifikatory formatu
"""
if size > multiple:
    return '{0:.1f} {1}'.format(size, suffix)
:.1f je format specifier - specifikatory obecne umoznuji upravit text: prida vycpavku z nul/mezer, zarovnat retezce,
ridit pocet desetinnych mist a konvertovat cisla do sestnactkove soustavy
: oznacuje zacatek specifikatoru formatu
.1 znamena zaokrouhli na 1 desetinne misto
f znamena cislo s pevnou radovou carkou (opak k exponencialnimu zapisu nebo jinymzpusobum reprezentace cisla) 
"""

a_string = 'user=pilgrim&database=master&password=Papaya'
a_list = a_string.split('&')
print(a_list)
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]  # 1 znamena rozdelit jen jednou
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)

# retezce v. bajty
"""
Bajty jsou bajty, znaky jsou abstrakce.
nemenitelna posloupnost Unicode znaku = retezec
nemenitelna posloupnost cisel z intervalu 0-255 = objekt typu bytes
"""
by = b'abcd\x65'
# definice objektu type bytes; bajtovy literal; kazdy bajt muze byt ASCII znak nebo zakodovane sestnactkove cislo
# od \x00 do \xff (0-255)
print(by)
print(type(by))
print(len(by))
by += b'\xff'  # objekty type bytes lze retezit
print(len(by))
print(by[0])  # funguje pouziti indexu; vraci 97 jako cislo pro a
# by[0] = 102 haze TypeError bytes object does not support assignment - objekt typu bytes je immutable/nemenitelny
# v pripade potreby lze pouzit slicing, kontatenaci a konverzi na bytearray

by = b'abcd\x65'
barr = bytearray(by)  # premena na objekt menitelneho typu bytearray
print(barr)
print(len(barr))
barr[0] = 102  # lze prirazovat
print(barr)  # 102 je v ASCII f

by = b'd'
s ='abcd'
# by += s bajty a retezce nelze michat, jsou to ruzne datove typy, haze TypeError
# s.count(by) TypeError - v retezci zadne bajty nejsou
print(s.count(by.decode('ascii')))
# spocitej vyskyty reteze, ktery byse dostal po dekodovani teto posloupnosti bajtu pri urcitem znakovem kodovani
"""
objekt typu bytes ma metodu decode() - prebere znakove kodovania vraci retezec
retezce majimetodu encode() - prebere znakove kodovani a vraci objekt typu bytes
"""
by = b'\xe6\xb7\xb1\xe5\x85\xa5 Python'  # pod timto sestnactkovym cislem jsou ty dva cinske znaky v utf-8
a_string = by.decode('utf-8')
print(a_string)
print(len(a_string))
print(len(by))

by = a_string.encode('gb18030')  # jina cisla plati pro jine kodovani - zcela jina posloupnost bajtu
print(by)
print(len(by))

by = a_string.encode('big5')  # a zase jina cisla pro jine kodovani - zcela jina posloupnost bajtu
print(by)
print(len(by))
roundtrip = by.decode('big5')
print(roundtrip)
print(roundtrip == a_string)

"""
Python3 interpretuje zdrojovy kod v kodovani utf-8. To lze zmenit deklaraci jineho kodovani:
# -*- coding: windows-1252 -*-
"""

