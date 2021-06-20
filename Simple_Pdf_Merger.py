# Simple PDF Merger in Python3
# Author: Sriharsha Kotcharlakot
# Date: Sun, 20 Jun 2021

import subprocess

def install(name):
    subprocess.call(['pip3', 'install', name])

try:
    from PyPDF4 import PdfFileReader, PdfFileWriter
except:
    install("PyPDF4")
    from PyPDF4 import PdfFileReader, PdfFileWriter

def merge_pdfs(pdf1_path, pdf2_path):
    pdf_writer = PdfFileWriter()
    pdf1_reader = PdfFileReader(pdf1_path, 'rb')
    pdf2_reader = PdfFileReader(pdf2_path, 'rb')

    for i in range(pdf1_reader.getNumPages()):
        page = pdf1_reader.getPage(i)
        pdf_writer.addPage(page)

    for i in range(pdf2_reader.getNumPages()):
        page = pdf2_reader.getPage(i)
        pdf_writer.addPage(page)

    with open('Resultant_PDF_After_Merging.pdf', 'wb') as fh:
        pdf_writer.write(fh)

    print("Merged the pdfs '" + path1 + "', and '" + path2 + "'.")

print("!!  Welcome to Simple PDF Page Remover  !!")

print("Enter path to the first PDF required for merging:")
path1 = input()

print("Enter path to the second PDF required for merging:")
path2 = input()

merge_pdfs(path1, path2)