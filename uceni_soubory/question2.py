with open('soubor', encoding='UTF-8') as text:
    content = text.read()
    lines = 0
    for line in content.split("\n"):
        if line and type(line[0]) == str:
            if line[0].islower():
                lines += 1


print(lines)

# grep -c '^[[:lower:]]' soubor
# grep -c '^[a-z]' soubor
