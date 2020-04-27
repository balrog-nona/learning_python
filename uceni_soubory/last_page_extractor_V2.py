#!/bin/python3

import PyPDF2
import sys
import os
import glob

# tato verze prejmenuje vsechny soubory ve slozce, vytvori nove a puvodni zachova
# pro verzi, co puvodni maze, je bash script linux_page_extractor

files = glob.glob("{}*.pdf".format(sys.argv[1]))  # absolutni cesta k souborum

for file in files:
    input_file = open(file, 'rb')
    directory, file_name = os.path.split(file)
    name, suf = os.path.splitext(file_name)

    input_reader = PyPDF2.PdfFileReader(input_file)
    writer = PyPDF2.PdfFileWriter()

    for pageNum in range(input_reader.numPages - 1):
        pageObj = input_reader.getPage(pageNum)
        writer.addPage(pageObj)

    new_file = open('{}/{}_new.pdf'.format(directory, name), 'wb')
    writer.write(new_file)
    input_file.close()
    new_file.close()

# jinak soubory se v pythonu mazou pomoci os.remove("nazev")
