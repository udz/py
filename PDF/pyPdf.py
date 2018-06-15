# pyPdf.py
# Opens two files and merges them and outputs third file named out.pdf

import PyPDF2

pdfFileObj1 = open('PDF/travelnxt-feature-list.pdf','rb')
pdfFileObj2 = open('PDF/ImePay_AirTicket_20180425.pdf','rb')

pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
pdfReader2 = PyPDF2.PdfFileReader(pdfFileObj2)
pdfWriter = PyPDF2.PdfFileWriter()

for page in range(pdfReader1.numPages):
    pageObj = pdfReader1.getPage(page)
    pdfWriter.addPage(pageObj)

for page in range(pdfReader2.numPages):
    pageObj = pdfReader2.getPage(page)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('PDF/out.pdf','wb')
pdfWriter.write(pdfOutputFile)

#print(pdfReader1.numPages)
#pageObj = pdfReader1.getPage(0)
#print(pageObj.extractText())

pdfOutputFile.close()  
pdfFileObj1.close()
pdfFileObj2.close()