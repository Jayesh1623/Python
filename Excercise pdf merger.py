from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
k= [file for file in os.listdir() if file.endswith(".pdf")]
print(k)
files = k #[file for file in os.listdir("TempFolder") if file.endswith(".pdf")]

for pdf in files:
    print(pdf)
    merger.append(pdf)
    
merger.write("merged-pdf.pdf")
merger.close()

