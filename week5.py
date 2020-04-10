# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:17:22 2020

@author: Dell
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
    
    
    
    
    



import urllib
from BeautifulSoup import *
import xml.etree.ElementTree as ET


actual_data = "http://py4e-data.dr-chuck.net/comments_427262.xml"

#We'll analyze this generic parameter, so we will only need to change its source
#and not every single one of its appearances in the code
#NOTE: I'm using Sublime Text and it doesn't accept raw_input, so I'll set the URL
#from here isntead from a user prompt
data_url = actual_data 
data = urllib.urlopen(data_url).read()

#xml_data contains the commentinfo object, as it is the main structure, so we 
#have to look for the comments element and then for all its comment elements
xml_data = ET.fromstring(data)
search_str = "comments/comment"
count_tags = xml_data.findall(search_str)

#Computing the sum
total_count = 0
for tag in count_tags:
	#We'll find the "count" element inside each "comment" element and add it 
	count = tag.find('count')
	total_count += int(count.text)

print(total_count)


    
    
    
    
    
    
