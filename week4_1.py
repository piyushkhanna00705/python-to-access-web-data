# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:00:27 2020

@author: Dell
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file



    




import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen


data_url = "http://py4e-data.dr-chuck.net/comments_427260.html"

#Getting the html information and parsing it with BeautifulSoup
html = urlopen(data_url).read()
soup = BeautifulSoup(html)

#Getting a list with the "span" tags
tags = soup('span')

#Counting the sum of all the values within the span tags
count = 0
for tag in tags:
	
	#We need to cast them to int, as they're parsed as text strings
	count += int(tag.contents[0])

print(count)



















