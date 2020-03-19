#Simple PDF To Audio Book Converter in Python3
#Author: Sriharsha Kotcharlakot
#Date: Thu, 19 Mar 2020

import subprocess

def install(name):
    subprocess.call(['pip3', 'install', name])
try:
    from PyPDF4 import PdfFileReader, PdfFileWriter
except:
    install("PyPDF4")
    from PyPDF4 import PdfFileReader, PdfFileWriter

try:
    from gtts import gTTS
except:
    install("gtts")
    from gtts import gTTS

def extract_text(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path, 'rb')
    file_writer = open('Intermediate_Text_Output_For_Audio_Conversion.txt', 'w')
    i = 0
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        content = page.extractText()
        file_writer.write(content)
    file_writer.close()
    print('Please be patient to endure several empty minutes! And be sure to have a stable internet connection.')
    file_reader = open('Intermediate_Text_Output_For_Audio_Conversion.txt', 'r')
    content = file_reader.read()
    language = 'en'
    gtts_obj = gTTS(text = str(content), lang = language, slow=False)
    gtts_obj.save("Audio_Book.mp3")
    print('Audio book has been generated and saved as Audio_Book.mp3')

print("!!  Welcome to Simple PDF To Audio Book Converter  !!")
print("Enter path to the required PDF:")
path = input()
extract_text(path)
