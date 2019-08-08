with open('soubor', encoding='UTF-8') as text:
    content = text.read()
    lines = 0
    for line in content.split("\n"):
        lines += 1
        if line and line[0].isupper():
            lines -= 1


print(lines)  # vraci 20, protoze vyhodnoti oba prazdne radky

# kolik radku nezacina velkym pismenem v souboru:
# grep -c -v '^[A-Z]' soubor   - vraci 19, ale nevyhodnoti prazdny radek na konci souboru
# grep -c '^[^[:upper:]]' soubor   - vraci 18 - nevyhodnoti prazdny radek ani uprostred souboru
# grep -c '^[^A-Z]' soubor  - vraci 18, dtto
