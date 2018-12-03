from pictures import pics


for i in range(10):
    with open("sibenice{}.txt".format(i), mode="w", encoding="utf-8") as novy_soubor:
        novy_soubor.write(pics[i])
