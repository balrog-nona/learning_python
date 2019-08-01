import PyPDF2
import os

files = []
for filename in os.listdir('../../../automate_online-materials/'):
    """
    os.listdir() vytvori seznam polozek, ktere se nachazeji ve slozce, krome specialnich jako . a ..
    """
    if filename.endswith('.pdf') and filename != 'encrypted.pdf':
        files.append(filename)

files.sort(key=str.lower)  # sorting list - alphabetical order

pdfWriter = PyPDF2.PdfFileWriter()

for file in files:
    pdf_reader = PyPDF2.PdfFileReader(open('../../../automate_online-materials/{}'.format(file), 'rb'))
    for pageNum in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(pageNum)
        pdfWriter.addPage(page_obj)

new_pdf = open('../../../automate_online-materials/allminutes.pdf', 'wb')
pdfWriter.write(new_pdf)
new_pdf.close()

