import requests

"""
Automate the boring stuff with Python - Chapter 11
"""

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')  # odkaz na stranku, kde je Romeo a Julie
print(type(res))
# requests.get() vraci Response object, ktery obsahuje response that the web server gave me for the request

# po get() je treba vyzkouset, jestli se povedlo
print(res.status_code == requests.codes.ok)  # status code 200
res.raise_for_status()  # lepsi zkouska, jestli get() probehlo ok. V pripade problemu vyvola vyjimku, jinak neudela nic.

# downloaded web page is stored as a text in Response object's text variable
print(len(res.text))
print(res.text[:250])

# priklad s nenalezenou strankou
res = requests.get('https://inventwithpython.com/non_existing_page')
# res.raise_for_status()  # vyhodi vyjimku a program spadne

# osetreni vyjimky, aby program nespadl
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {}'.format(exc))  # exit code 0, cili nenastala chyba


# ulozeni stahnuteho souboru
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

with open('RomeoAJulie.txt', 'wb') as new_file:
    for chunk in res.iter_content(100000):  # 100000 bytes of data will contain every chunk
        new_file.write(chunk)

"""
each chunk is of the bytes data type
Kdyz je obsah stranky stahnuty, tak jsou to uz data v mem programu, tj. i kdyz ztratim pripojeni k internetu, data
zustanou.
"""