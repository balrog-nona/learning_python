from pictures import pics

"""
Jednorazovy program, ktery vytvoril 10 souboru z jednoho modulu, ktery obsahoval jen promennou pics, ktera
obsahovala obrazky jako polozky v seznamu.
Tento soubor je uz obsolentni.
"""

for i in range(10):
    with open("sibenice{}.txt".format(i), mode="w", encoding="utf-8") as novy_soubor:
        novy_soubor.write(pics[i])
