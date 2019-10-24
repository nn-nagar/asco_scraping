import time
from pynput.keyboard import Key,Controller
from bs4 import BeautifulSoup
import csv
import requests



html = requests.get("https://cancerres.aacrjournals.org/content/76/14_Supplement/5200")


time.sleep(2)


soup = BeautifulSoup(html.text, 'lxml')

print("---------------------------------------------------------------------------------------------------------------------")

title = soup.title.text
print('Title : ',title)

print()
print("---------------------------------------------------------------------------------------------------------------------")

PIS_and_presenter = soup.find("div", class_="highwire-cite-authors")
if PIS_and_presenter is None:
    PIS_and_presenter = ""
else:
    PIS_and_presenter = PIS_and_presenter.text
print("PIS_and_Presentere : "+PIS_and_presenter)
print()
print("---------------------------------------------------------------------------------------------------------------------")


medicalCenter = soup.find('p',id="p-8")
if medicalCenter is None:
    medicalCenter = ""
else:
    medicalCenter.text.strip()
print("MedicalCenter :"+ str(medicalCenter))
print()
print("---------------------------------------------------------------------------------------------------------------------")


publish_date = soup.find("div",class_="issue-title")
if publish_date is None:
    publish_date=""
else:
    publish_date = publish_date.text.strip()
print("Publish_date :"+ publish_date)

print("---------------------------------------------------------------------------------------------------------------------")


with open(r"HtmlData.csv",'w') as csvfile:
    fieldnamessss = ['Title','NamPIS_and_Presentere','MedicalCenter','Publish_date']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnamessss)
    writer.writeheader()
    writer.writerow({'Title':title,'NamPIS_and_Presentere': PIS_and_presenter,'MedicalCenter': medicalCenter,'Publish_date': publish_date})

 

