import docx

"""
data types:
1. Document object - represents the entire document. Contains a list of:
2. Paragraph objects - for the paragraphs; new paragraph begins whenever the user presses enter or return while typing
Each paragraph object contains a list of:
3. Run objects - contiguous run of text with the same style. A new object is needed whenever the text style changes
"""

# reading document
doc = docx.Document('../../../automate_online-materials/demo.docx')
print(len(doc.paragraphs))  # 7 paragraph objects in the document
print(doc.paragraphs[0].text)
print(doc.paragraphs[1].text)
print(len(doc.paragraphs[1].runs))  # pocet run objectu v prvnim paragraphu

for item in doc.paragraphs[1].runs:
    print(item.text)

print('---------------------------------------------')

# pro prostou extrakci textu bez ohledu na jeho cleneni si napisu fci getText()
def getText(finemane):
    """
    Da se prizpusobit i tak, aby text nejak modifikovala
    """
    doc = docx.Document(finemane)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

print(getText('../../../automate_online-materials/demo.docx'))

# styling
"""
Paragraph styles can be applied to Paragraph objects
Character styles can be applied to Run objects
linked styles to both
dela se to tak, ze priradim atribut style to Paragraph or Run object. je preddefinovane, jak ten atribut muze znit

Runs can be further styled using text attributes - 3 values: True, False, None
"""




