from lxml import html
import numpy as np
import json
import requests

page = requests.get('https://maps.raleighnc.gov/arcgis/rest/services/Planning/Zoning/MapServer/0/query?where=1%3D1&outFields=ZONE_TYPE&outSR=4326&f=json')
if page.status_code == 200:
    print("Connection Successful")
else:
    print("Bad Connection")

page.encoding = 'utf-8'
print(page.headers)
