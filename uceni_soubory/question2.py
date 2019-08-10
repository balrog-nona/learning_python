import re

with open('soubor', encoding='UTF-8') as text:
    content = text.read()
    lines = 0
    for line in content.splitlines():  # split('\n') vracelo i posledni line break jako samostatny radek
        lines += 1
        if line and line[0].isupper():
            lines -= 1

print(lines)  # vraci 32

with open('soubor', encoding='UTF-8') as text:
    content = text.read()
    lines = 0
    for line in content.splitlines():
        if not line or not line[0].isupper():
            lines += 1

print(lines)  # vraci 32

with open('soubor', encoding='UTF-8') as text:
    content = text.read()
    lines = 0
    for line in content.splitlines():
        lines += 1
        pattern = '[A-Z]'
        if line and re.search(pattern, line[0]):
            lines -= 1

print(lines)  # vraci 32


with open('soubor', encoding='UTF-8') as text:
    content = text.read()
    lines = 0
    for line in content.splitlines():
        pattern = '(^[^A-Z]|^$)'
        if re.search(pattern, line):
            lines += 1

print(lines)  # vraci 32


# kolik radku nezacina velkym pismenem v souboru: 32 by mel byt spravny vysledek i ve vztahu k prazdnym radkum
# grep -c -v '^[A-Z]' soubor   - vraci spravne 32

# nefungovalo:
# grep -c '^[^[:upper:]]' soubor   - vraci 20, nevyhodnoti prazdne radky
# grep -c '^[^A-Z]' soubor  - vraci 20 kvuli prazdnym radkum

# 1. varianta zapisu
# grep -c -e '^[^[:upper:]]' -e '^$' soubor  - vraci 32, dva regularni vyrazy po sobe matchnou i prazdne radky
# grep -c -e '^[^A-Z]' -e '^$' soubor  - vraci 32

# 2. varianta zapisu
# grep -c '^[^[:upper:]]\|^$' soubor
# grep -c '^[^A-Z]\|^$' soubor

# na soubory, kde prazdne radky nejsou, funguji ty prikazy grepu stejne

