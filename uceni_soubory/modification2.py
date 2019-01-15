import glob
import os

songs = glob.glob("*/*/*/*.txt")  # vraci seznam cest pro kazdou pisen jednotlive

for song in songs:
    directory, file = os.path.split(song)
    name, suf = os.path.splitext(file)
    with open(song, encoding="utf-8") as text:
        content = text.read()
        counting_lines = 0
        for line in content.strip().split("\n"):
            counting_lines += 1
        print("{}: {}".format(name, counting_lines))
        if "Eminem" in content:
            print("Eminem: {}\n".format(name))
