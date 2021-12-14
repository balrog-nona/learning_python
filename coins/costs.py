#!/usr/bin/python3

def prumer_coinu(seznam_nakupu):
    souhrnna_hodnota = 0
    souhrnny_pocet = 0
    for nakup in seznam_nakupu:
        souhrnna_hodnota += nakup['hodnota']
        print(souhrnna_hodnota)
        souhrnny_pocet += nakup['pocet']
        print(souhrnny_pocet)
    prumer = souhrnna_hodnota / souhrnny_pocet
    return round(prumer)


def average_costs(seznam_prodeju, seznam_nakupu):
    zisk = 0
    prumerna_cena = prumer_coinu(seznam_nakupu)
    print(prumerna_cena)
    for prodej in seznam_prodeju:
        vynos_z_prodeje = prodej['cena_za_kus'] * prodej['pocet']
        naklad_na_prodej = prumerna_cena * prodej['pocet']
        zisk += vynos_z_prodeje - naklad_na_prodej
    return zisk