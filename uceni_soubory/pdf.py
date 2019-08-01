import PyPDF2

"""
Dle knizky: automate the boring stuff with python
https://automatetheboringstuff.com/chapter13/
vice v dokumentaci
"""


pdfFileObj = open('../../../automate_online-materials/meetingminutes.pdf', 'rb')  # rb read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)  # cisluje se od 0 a bez ohledu na cisla stranek
print(pageObj.extractText())

# encryption
reader = PyPDF2.PdfFileReader(open('../../../automate_online-materials/encrypted.pdf', 'rb'))
print(reader.isEncrypted)  # vraci True/False
# print(reader.getPage(0)) hodi error
reader.decrypt('rosebud')  # decrypts only the reader object, not the file itself
pageObj = reader.getPage(0)
print(pageObj.extractText())

# creating pdf
"""
counterpart k PdfFileReader je PdfFileWriter object
nelze zapsat text do pdf, ale jen kopirovat stranky z existujicich pdf, otecet strany, heslovat apod. 
nelze primo editovat pdf - lze jen vytvorit nove a kopirovat obsah z existujicicho dokumentu
Postup:
1. otevrit pdf pomoci PdfFileReader object
2. vytvorit PdfFileWriter object - vytvori objekt, ne primo ten soubor
3. kopirovat strany z PdfFileReader do PdfFileWriter
4. pomoci PdfFileWriter vytvorit pdf
"""
# 1. kopirovani stranek
pdf1File = open('../../../automate_online-materials/meetingminutes.pdf', 'rb')
pdf2File = open('../../../automate_online-materials/meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()  # blank pdf document

for pageNum in range(pdf1Reader.numPages):  # kopirovani stran prvniho pdf
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):  # kopirovani stran druheho pdf
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('../../../automate_online-materials/combinedminutes.pdf', 'wb')  # wb write binary mode
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

# 2. rotating pages
"""
rotace po 90 stupnich, tj. 90, 180, 270
rotateClockwise() nebo rotateCounterClockwise()
"""
minutesFile = open('../../../automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('../../../automate_online-materials/rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

# 3. overlaying pages - useful for adding the logo, timestamp, watermark...
minutes_file = open('../../../automate_online-materials/meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)
minutes_first_page = pdf_reader.getPage(0)
watermark_reader = PyPDF2.PdfFileReader(open('../../../automate_online-materials/watermark.pdf', 'rb'))
minutes_first_page.mergePage(watermark_reader.getPage(0))
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(minutes_first_page)

for pageNum in range(1, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(pageNum)
    pdf_writer.addPage(page_obj)

result_file = open('../../../automate_online-materials/watermarkedCover.pdf', 'wb')
pdf_writer.write(result_file)
minutes_file.close()
result_file.close()

# 4. encrypting files
"""
Vysledkem nebude existujici pdf zaheslovane, ale obsah pdf, ktere chci zaheslovat, zkopirovany do noveho pdf a toto
pak zaheslovane.
"""
pdf_reader = PyPDF2.PdfFileReader(open('../../../automate_online-materials/meetingminutes.pdf', 'rb'))
pdf_writer = PyPDF2.PdfFileWriter()

for pageNum in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(pageNum))

pdf_writer.encrypt('swordfish')
new_pdf = open('../../../automate_online-materials/encryptedminutes.pdf', 'wb')
pdf_writer.write(new_pdf)
new_pdf.close()


