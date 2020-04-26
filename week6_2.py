# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:59:53 2020

@author: Dell
"""

import json
import urllib.request, urllib.parse, urllib.error
import requests

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


#Storing the given parameters
sample_address = "South Federal University"
data_address = "Nagpur University"
address_wanted = data_address

#Setting the GET parameters on the URL
parameters = {"sensor": "false", "address": address_wanted}
parameters['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parameters)

#Generating the complete URL. Printing it in order to check if it's correct.
print("DATA URL: ", url)


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')


#Obtaining and reading the data
jsondata=requests.get(url).json()

place_id = jsondata["results"][0]["place_id"]
print("PLACE ID: ", place_id)
