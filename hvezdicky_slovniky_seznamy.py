slovnik = {"jmeno": "Lucka", "povolani": "drticka odpadu", "zajmy": "kresleni"}
print("{jmeno} pracuje jako {povolani} a ma rada {zajmy}.".format(**slovnik))

seznam = ["Marek", "Matous", "Lukas", "Jan"]
print("{0}, {1}, {2} a [3] si sedli a napsali knizku.".format(*seznam))
