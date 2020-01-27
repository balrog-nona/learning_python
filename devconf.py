import numpy as np
import pandas as pd

# http://bit.ly/python-data-notebooks - github repository s prikladama

"""
Mluvilo se o array v NumPy:
a = NumPy.array([1,2,3,4])

Slicing in NumPy (np) doesn't give me a new list/array, it just points to the existing one.
Changing a value in sliced array will change the original array too because the slice just points to the same space
in memory s the original.
"""
a = max([1,1,5,9],[1,2,4,6])  # porovnava ty dva listy hodnotu po hodnote
print(a)

b = np.maximum([1,1,5,9],[1,2,4,6])  # bere nejvetsi elementy z obou
print(b)

np.array([1,2,5,9]) * 3  # vynasobi kazdy element
np.array([1,2,5,9]) * np.array([1,2,5,9])  # vynasobi prvky proti sobe

a = pd.Series(['beta', 'gamma', 'delta'])
print(a)
a.index = ['b','g', 'd']

# PANDAS
"""
tabulky Dataframe
.loc - pristup k row
elementwise arithmetic .apply(lambda ...)

tidy data - 3 rules: 
each variable forms a column (day 1,day 2, day3 -> day varible)
each observation forms a row
each type of observational unit forms a table
"""

