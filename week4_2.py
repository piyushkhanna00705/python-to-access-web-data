# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:09:59 2020

@author: Dell
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl





problem_url = "http://py4e-data.dr-chuck.net/known_by_Jia.html"
problem_repetitions = 7
problem_resultPosition = 18

(link, repetitions, resultPosition) = (problem_url, problem_repetitions, problem_resultPosition)


#Amount of iterations needed
for times in range(repetitions):

	
	html = urllib.request.urlopen(link).read()
	soup = BeautifulSoup(html)
	tags = soup('a')

	link = tags[resultPosition - 1].get('href')

result_name = tags[resultPosition - 1].contents[0]
print(result_name)