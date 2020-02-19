#Simple PDF Page Remover in Python3
#Author: Sriharsha Kotcharlakot
#Date: Sun, 16 Feb 2020

from PyPDF4 import PdfFileReader, PdfFileWriter

def remove_page(pdf_path, page_numbers):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path, 'rb')
    i=0
    for page in [pdf_reader.getPage(i) for i in range(pdf_reader.getNumPages())]:
        if not i in page_numbers:
            pdf_writer.addPage(page)
        i+=1
    with open('Resultant_PDF_After_Removal.pdf', 'wb') as fh:
        pdf_writer.write(fh)

print("!!  Welcome to Simple PDF Page Remover  !!")
print("Enter path to the required PDF:")
path = input()
print("Enter the page numbers (starting from 0) that are required to be removed delimiting with spaces (For Example: 0 2 3 4 67 34):")
page = list(map(int, input().split()))
remove_page(path, page)
