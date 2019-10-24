# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('AllAbstracts_2018-12-03_Updated.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(0)

title = pageObj.extractText()[68:141]
print("Title  :"+title)

print("-------------------------------------------------------------------------------------------------------------------------------")
# extracting text from page 
PIS_and_presenter = pageObj.extractText()[141:253]
print("PIS_and_Presentere :     "+PIS_and_presenter)
# closing the pdf file object 
print("-------------------------------------------------------------------------------------------------------------------------------")

medicalCenter = pageObj.extractText()[253:388]
print("MedicalCenter  :  "+medicalCenter)

print("-------------------------------------------------------------------------------------------------------------------------------")

publish_date = pageObj.extractText()[:41]
print("publish_date  :"+publish_date)

pdfFileObj.close() 


