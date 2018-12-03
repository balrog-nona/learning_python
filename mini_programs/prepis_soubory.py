def prepis(): 
    with open("basnicka.txt", mode="w", encoding= "utf-8") as soubor:
        print("Nase stare hodiny", file=soubor)
        print("Biji", 2 + 2, "hodiny.", end="", file=soubor)
        
"""
nebo soubor.write("text\n")
"""
        
def precti():
    with open("basnicka.txt", encoding="utf-8") as soubor:
        obsah = soubor.read()
        print(obsah) 
        
prepis()
precti()
