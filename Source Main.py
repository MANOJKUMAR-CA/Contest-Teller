# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:21:39 2022

@author: Bala
"""

from bs4 import BeautifulSoup
import requests

URL = {"test":"https://webscraper.io/test-sites/e-commerce/allinone", 1:"http://www.collegeevents.info/search-events"};

page = requests.get(URL[1])
soup = BeautifulSoup(page.content,"html.parser")

print(soup)