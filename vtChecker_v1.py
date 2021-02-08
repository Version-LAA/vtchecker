import requests
import time
from csv import reader
import pandas as pd

import json

'''*****To use this script, please do the following:
STEP 1: Enter your file name that contains your list of IP's, be sure to place it in
between the quotes i.e. file_name = 'ip_list.csv' 
 
STEP 2: Enter your VirusTotal Api Key below i.e. api_key = '1234567890abcdefghijklmnopqrstuv'

 ******'''



# Enter your file name and api key in the variables below:

file_name = '<PLACE FILENAME HERE (I.E.IP.CSV)>'
api_key = '<PLACE API_KEY HERE>'

# Open and read IP list
open_file = open(file_name)
read_file = reader(open_file)
ip_list = list(read_file)
u = 'https://www.virustotal.com/vtapi/v2/ip-address/report'


results = []

limit = 4

count = 0

# Performs a lookup of each ip in list to VirustTotal, free API Key limits # of request within one min

print("** Welcome to the Virustotal Checker for free API Keys!!** \n")

for ip in ip_list:
    count +=1
    print('Checking IP: ', ip)
    p = {'apikey': api_key, 'ip': ip}
    r = requests.get(u, p)
    results.append(r.json())
    if count == limit:
        print("you're using a free api key - this may take some time")
        time.sleep(65)
        print('ok, back to work....')

data = [['ip','owner','country', '#_detected_urls']]
c = 0
t = len(ip_list)

# Parses json responses from virustotal
for i in results:
    as_owner = i['as_owner']
    country = i["country"]
    ip = ip_list[c]
    detected_urls = i['detected_urls']

    num_of_detections = 0
    for d in detected_urls:
        num_of_detections +=1
    data.append([ip, as_owner, country, num_of_detections])
    c += 1

# creates a dataframe of results
df = pd.DataFrame(data)

print("Here's your Data, a CSV has also been created name ipvtresults.csv")

for i in data:
    print(i)

#Creates a csv of results
df.to_csv('ipvtresults.csv')

