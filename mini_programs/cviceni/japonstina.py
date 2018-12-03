"""
Nepochopila jsem zadani, tak jsem si s tim pohrala po svem.
Program nedava smysl bez souboru rozsypany_caj.txt, ktery musi obsahovat nejaky japonsky text, treba z wikipedie.
"""


hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔ"

katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ"

pocet_h = 0
pocet_k = 0

soucet_h = 0
soucet_k = 0

with open("rozsypany_caj.txt", encoding="utf-8") as obsah:
    text = obsah.read()
    for pismeno in hiragana: # kolik druhu znaku se nachazi v textu
        if pismeno in text:
            pocet_h += 1
    for pismeno in katakana:
        if pismeno in text:
            pocet_k += 1
            
    for pismeno in text: # do ktere abecedy spadaji jednotlive pismena v textu
        if pismeno in hiragana:
            soucet_h +=1
        if pismeno in katakana:
            soucet_k += 1
            
    delka_textu = len(text) # zrejme do delky pocita i mezery
  
            
print("katakana: ", pocet_k, "druhu znaku")
print("hiragana: ", pocet_h, "druhu znaku\n")
print("katakana: ", soucet_k, "x")
print("hiragana: ", soucet_h, "x")
print("soubor ma ", delka_textu, "znaku")



