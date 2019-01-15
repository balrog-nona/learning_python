import glob

songs = glob.glob("*/*/*/*.txt", recursive=True)  # pozor, cesta musi byt jako string!

"""
takto by vypadala verze, kdyby ty pisnicky byly ulozene nekde cestou nahoru a pak jeste uplne jinam:
songs = glob.glob("../../../../../Videa/Seriály/*/*/*/*.txt")
"""

print(type(songs))  # glob.glob evidentne vytvori seznam

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
