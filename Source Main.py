# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:21:39 2022

@author: Bala
"""
import json
from bs4 import BeautifulSoup
import requests

def printData(data):
    for i in data:
        strtext = i["name"] + "|| SD: " + i['startDate'] + "|| LOC: " +i['location']['@type']
        print(strtext)
        for i in range(0,len(strtext)):
            print("-",end="")
        print()


URL = {"test":"https://webscraper.io/test-sites/e-commerce/allinone", "Event":"http://www.collegeevents.info/search-events", "Hack":"https://www.eventbrite.com/d/online/science-and-tech--events/hackathon/?page=1"};

page = requests.get(URL["Hack"])
soup = BeautifulSoup(page.content,"html.parser")

data = json.loads(soup.find('script', type='application/ld+json').text)

printData(data)