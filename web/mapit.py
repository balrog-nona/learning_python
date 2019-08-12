#!/usr/bin/python3

import webbrowser
import sys
import pyperclip

"""
Automate the boring stuff with Python Chapter 11
Tvorba programu, ktery vezme zadanou adresu z prikazoveho radku nebo ze chranky a otevre google maps s touto adresou.
Pristup k programu by mel byt v prikazove radce nasledujici:
mapit 870 Valencia St, San Francisco, CA 94110   - v takovem pripade vezme argumenty z prikazove radky;
jinak ze schranky
"""

# 1. handle command line arguments
if len(sys.argv) > 1:  # sys.argv[0] ulozi program's filename
    # get address from command line, e. g. address has been given
    # sys.argv by vypadal takto: ['mapit.py', '870', 'Valencia', 'St, ', 'San', 'Francisco', 'CA', '94110']
    address = " ".join(sys.argv[1:])  # vrati 1 string: '870 Valencia St, San Francisco, CA 94110'
else:
    # vlozit adresu ze schranky - clipboard
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)
