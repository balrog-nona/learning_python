"""
Funguje, opravdu vytvoří nový soubor.
"""

puvodni_soubor = input("Ktery soubor chces zkopirovat?")
puvodni_soubor = puvodni_soubor.strip()

novy_soubor = input("Jak se ma jmenovat novy soubor?")
novy_soubor = novy_soubor.strip()

with open(puvodni_soubor, encoding="utf-8") as text:
    obsah = text.read()
    
with open(novy_soubor, mode="w", encoding="utf-8") as novy:
    novy.write(obsah)
    
    
