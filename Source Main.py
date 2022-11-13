# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:21:39 2022

@author: Bala
"""
import json
import openpyxl
from bs4 import BeautifulSoup
import requests


'''excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Hackathon lists"
sheet.append(['Name','SD','ED','LOCATION'])'''


def printData(data):
    for i in data:
        strtext = i["name"] + "|| SD: " + i['startDate'] +"|| ED:"+i['endDate']+"|| LOC: " +i['location']['@type']
        print("[+]"+strtext)
        #sheet.append([i['name'],i['startDate'],i['endDate'],i['location']['@type']])
        for i in range(0,len(strtext)):
            print("*",end="")
        print()


#URL = {"test":"https://webscraper.io/test-sites/e-commerce/allinone", "Event":"http://www.collegeevents.info/search-events", "Hack":["https://www.eventbrite.com/d/online/science-and-tech--events/hackathon/?page=1","https://www.eventbrite.com/d/online/science-and-tech--events/hackathon/?page=2"]};
#url="https://www.eventbrite.com/d/online/science-and-tech--events/hackathon/?page="
search=input("Enter what you Need :")
url="https://www.eventbrite.com/d/online/"+search+"/?page="

'''page=requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
lastpage=soup.find('li').find('span',class_="eds-text-color--control eds-text-weight--heavy").text
print(lastpage) '''

res = 0
lastpage=228
try:
    for i in range(1,lastpage):
        furl=url+str(i)
        page = requests.get(furl)
        soup = BeautifulSoup(page.text,"html.parser")
        data = json.loads(soup.find('script', type='application/ld+json').text)
        printData(data)
        res+=1
except:
    print("[-]Error occured.. terminating")
finally:
    print("[+]Total results: "+ str(res) +"\n[+]Closing application")


#excel.save("Project.xlsx")