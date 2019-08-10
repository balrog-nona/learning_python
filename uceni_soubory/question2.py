with open('soubor', encoding='UTF-8') as text:
    content = text.read()
    lines = 0
    for line in content.split("\n"):
        lines += 1
        if line and line[0].isupper():
            lines -= 1


print(lines)  # vraci 28, protoze vyhodnoti vsechny prazdne radky

# kolik radku nezacina velkym pismenem v souboru:
# grep -c -v '^[A-Z]' soubor   - vraci 27, ale nevyhodnoti 1 prazdny radek zrejme na konci souboru
# grep -c '^[^[:upper:]]' soubor   - nevyhodnoti prazdny radek ani uprostred souboru
# grep -c '^[^A-Z]' soubor  - dtto

# 28 by mel byt spravny vysledek i ve vztahu k prazdnym radkum
# vim soubor vyhodnucuje, ze ma jen 41 radku
