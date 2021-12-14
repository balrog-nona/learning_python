#!/usr/bin/python3

#import pytest
import costs

transakce1 = {'type': 'nakup', 'datum': '1.1.2021', 'mena': 'ETH', 'pocet': 0.8, 'cena_za_kus': 1000.0,
              'hodnota': None}
transakce1['hodnota'] = transakce1['cena_za_kus'] * transakce1['pocet']

transakce2 = {'type': 'nakup', 'datum': '1.2.2021', 'mena': 'ETH', 'pocet': 0.5, 'cena_za_kus': 2000.0,
              'hodnota': None}
transakce2['hodnota'] = transakce2['cena_za_kus'] * transakce2['pocet']

transakce3 = {'type': 'prodej', 'datum': '1.3.2021', 'mena': 'ETH', 'pocet': 0.3, 'cena_za_kus': 3000.0,
              'hodnota': None}
transakce3['hodnota'] = transakce3['cena_za_kus'] * transakce3['pocet']

transakce4 = {'type': 'prodej', 'datum': '1.4.2021', 'mena': 'ETH', 'pocet': 0.9, 'cena_za_kus': 4000.0,
              'hodnota': None}
transakce4['hodnota'] = transakce4['cena_za_kus'] * transakce4['pocet']

nakupy = list()
prodeje = list()


def roztrid_transakce(transakce, seznam_nakupu, seznam_prodeju):
    if transakce['type'] == 'nakup':
        seznam_nakupu.append(transakce)
    elif transakce['type'] == 'prodej':
        seznam_prodeju.append(transakce)


roztrid_transakce(transakce1, nakupy, prodeje)
roztrid_transakce(transakce2, nakupy, prodeje)
roztrid_transakce(transakce3, nakupy, prodeje)
roztrid_transakce(transakce4, nakupy, prodeje)


def test_prumer_coinu():
    assert costs.prumer_coinu(nakupy) == 1385


def test_average_costs():
    assert costs.average_costs(prodeje, nakupy) == 2838

nakup = {'type': 'nakup', 'datum': '1.6.2021', 'mena': 'ETH', 'pocet': 0.1, 'cena_za_kus': 1385.0,
              'hodnota': None}
nakup['hodnota'] = nakup['cena_za_kus'] * nakup['pocet']

novy_nakup = {'type': 'nakup', 'datum': '1.7.2021', 'mena': 'ETH', 'pocet': 0.5, 'cena_za_kus': 3000.0,
              'hodnota': None}
novy_nakup['hodnota'] = novy_nakup['cena_za_kus'] * novy_nakup['pocet']

penezenka = list()
penezenka.append(nakup)
penezenka.append(novy_nakup)


def test_prumer_coinu2():
    assert costs.prumer_coinu(penezenka) == 2731