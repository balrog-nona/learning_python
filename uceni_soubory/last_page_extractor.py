import PyPDF2

# ke scriptu existuje i bash script linux_page_extractor pro hromadnou zmenu u vice souboru naraz

input_file = open('input.pdf', 'rb')
input_reader = PyPDF2.PdfFileReader(input_file)
writer = PyPDF2.PdfFileWriter()

for pageNum in range(input_reader.numPages - 1):
    pageObj = input_reader.getPage(pageNum)
    writer.addPage(pageObj)

new_file = open('new.pdf', 'wb')
writer.write(new_file)
input_file.close()
new_file.close()
