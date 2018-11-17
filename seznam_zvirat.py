import pytest


zvirata_1 = ["pes", "kocka", "kralik", "had"]
zvirata_2 = ["kun", "kocka"]


def porovnani(list_1, list_2):
  spojeny_list = list_1 + list_2
  oba_seznamy = []
  jen_prvni = []
  jen_druhy = []
  for zvire in list_1: 
    if spojeny_list.count(zvire) > 1:
      oba_seznamy.append(zvire)
    elif zvire in list_1 and zvire not in list_2:
      jen_prvni.append(zvire)
  for zvire in list_2:
    if zvire in list_2 and zvire not in list_1:
      jen_druhy.append(zvire)
  return oba_seznamy, jen_prvni, jen_druhy
     

def test_porovnani():
    animals1 = ["snake", "horse", "goat"]
    animals2 = ["goat", "cow", "horse"]
    assert porovnani(animals1, animals2) == (["horse", "goat"], ["snake"], ["cow"])

 

print(porovnani(zvirata_1, zvirata_2))
