#!/usr/bin/python3


def fifo_coin(seznam_nakupu, seznam_prodeju):
    zisk = 0
    for prodej in seznam_prodeju:
        naklad_na_prodej = 0
        vynos_z_prodeje = prodej['cena_za_kus'] * prodej['pocet']

        while prodej['pocet'] > 0:
            if prodej['pocet'] < seznam_nakupu[0]['pocet']:
                naklad_na_prodej += seznam_nakupu[0]['cena_za_kus'] * prodej['pocet']
                seznam_nakupu[0]['pocet'] = seznam_nakupu[0]['pocet'] - prodej['pocet']
                prodej['pocet'] = 0
            if prodej['pocet'] >= seznam_nakupu[0]['pocet']:
                naklad_na_prodej += seznam_nakupu[0]['cena_za_kus'] * seznam_nakupu[0]['pocet']
                prodej['pocet'] = prodej['pocet'] - seznam_nakupu[0]['pocet']
                del seznam_nakupu[0]

        zisk += vynos_z_prodeje - naklad_na_prodej
    return zisk


