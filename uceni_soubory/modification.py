import glob

# relativni cesta k souborum
songs = glob.glob("*/*/*/*.txt", recursive=True)  # pozor, cesta musi byt jako string!

"""
takto by vypadala verze, kdyby ty pisnicky byly ulozene nekde cestou nahoru a pak jeste uplne jinam:
songs = glob.glob("../../../../../Videa/Seriály/*/*/*/*.txt") - ve forme relativni cesty

glob.glob se da pouzit jednak na relativni, tak na absolutni cesty + daji se pouzit wildcards
"""

#absolutni cesta k souborum
#songs = glob.glob("/home/balrog/Dokumenty/Programování/doGIThubu/learning_python/uceni_soubory/pisne/pisnicky/"
                  #"songs/*.txt")

print(type(songs), len(songs))  # glob.glob evidentne vytvori seznam

for song in songs:
    with open(song, encoding="utf-8") as text:
        content = text.read()
        counting_lines = 0
        # print(type(content))  # je to str
        # print(type(song))  # je to str
        for line in content.strip().split("\n"):
            counting_lines += 1
        print("{}: {} lines".format(song, counting_lines))
        if "Eminem" in content:
            print("Eminem: {} \n".format(song))
