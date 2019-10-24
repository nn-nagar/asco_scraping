from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  
from pynput.keyboard import Key,Controller
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import json

driver = webdriver.Firefox()
driver.get("https://meetinglibrary.asco.org/record/174960/abstract")
time.sleep(5)

with open('personal.json', 'w') as json_file:

    time.sleep(2)
    

    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')

    currentUrl = driver.current_url
    driver.get(currentUrl)
    time.sleep(2)

    print("-------------------------------------------------------------------------------------------------------------------------------")

    title=soup.find("h1", class_="ng-tns-c9-2")
    if title is None:
        title = ""
    else:
        title= title.get_text().strip()
    print("Title : "+title)
    print("-------------------------------------------------------------------------------------------------------------------------------")


    PIS_and_presenter=soup.find("div", class_="authors")
    if PIS_and_presenter is None:
        PIS_and_presenter = ""
    else:
        PIS_and_presenter= PIS_and_presenter.get_text().strip()

    print("PIS_and_Presentere : "+PIS_and_presenter)
    print("-------------------------------------------------------------------------------------------------------------------------------")


    medicalCenter=soup.find("div", class_="authors")
    if medicalCenter is None:
        medicalCenter = ""
    else:
        medicalCenter= medicalCenter.get_text().strip()
    print("MedicalCenter : "+medicalCenter)
    print("-------------------------------------------------------------------------------------------------------------------------------")


    published_data = soup.find("div",class_="date ng-tns-c9-2 ng-star-inserted")
    if published_data is None:
        published_data=""
    else:
        published_data = published_data.get_text().strip()
    print("published_data :" +published_data)
    print("-------------------------------------------------------------------------------------------------------------------------------")



    print("Link : "+currentUrl)
    print("-------------------------------------------------------------------------------------------------------------------------------")

    my_details = {
    "Title" : title,
    "PIS_and_Presentere" : PIS_and_presenter,
    "MedicalCenter" : medicalCenter,
    "published_data" : published_data,
    "Link" : currentUrl
    }
    json.dump(my_details, json_file)


     