#Simple PDF Page Remover in Python3
#Author: Sriharsha Kotcharlakot
#Date: Wed, 18 Mar 2020

from PyPDF4 import PdfFileReader, PdfFileWriter

def extract_text(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path, 'rb')
    f = open('out.txt', 'w')
    i=0
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        content = page.extractText()
        f.write(content)

print("!!  Welcome to Simple PDF Page Remover  !!")
print("Enter path to the required PDF:")
path = input()
extract_text(path)
