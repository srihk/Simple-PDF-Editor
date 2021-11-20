# Simple PDF Page Extractor in Python3
# Author: Sriharsha Kotcharlakot
# Date: Wed, 19 Feb 2020

import subprocess

def install(name):
    subprocess.call(['pip3', 'install', name])

try:
    from PyPDF4 import PdfFileReader, PdfFileWriter
except:
    install("PyPDF4")
    from PyPDF4 import PdfFileReader, PdfFileWriter

def remove_page(pdf_path, page_numbers):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path, 'rb')
    i=0
    for page in [pdf_reader.getPage(i) for i in range(pdf_reader.getNumPages())]:
        if i in page_numbers:
            pdf_writer.addPage(page)
        i+=1
    with open('Resultant_PDF_After_Extraction.pdf', 'wb') as fh:
        pdf_writer.write(fh)

print("!! Welcome to the pdf extractor ")
print("Enter path to the required for the PDF:")
path = input()
print("Enter the page numbers (from 0) that are required to be extracted delimiting with spaces (For Example: 0 2 3 4 67 34):")

page = list(map(int, input().split()))
remove_page(path, page)
