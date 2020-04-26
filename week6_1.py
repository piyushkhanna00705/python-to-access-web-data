# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:42:12 2020

@author: Dell
"""


import json
import urllib.request, urllib.parse, urllib.error
import requests

count = 0
total = 0

url = input("Enter Url - ")



data_url = "http://py4e-data.dr-chuck.net/comments_427263.json"

data=requests.get(data_url).json()


total = 0
for comment in data["comments"]:
	total += comment["count"]

print("TOTAL SUM: ", total)