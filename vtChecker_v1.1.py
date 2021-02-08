import requests
import datetime as dt
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

file_name = '<<**ENTER YOUR FILE NAME HERE**>>'
api_key = '<<**ENTER YOUR API KEY HERE**>>'


def intake_file(file):
    # Open and read IP list
    open_file = open(file)
    read_file = reader(open_file)
    ip_list = list(read_file)

    return ip_list


# Performs a lookup of each ip in list to VirustTotal, free API Key limits # of request within one min


def vt_caller():
    count = 0
    limit = 4
    ip_list = intake_file(file_name)
    results = []
    print('The program is loading up your ', str(len(ip_list)), ' IP addresses')
    time.sleep(15)
    api = api_key
    u = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    print('looks like there are ', len(ip_list), ' IP\'s to check')
    for ip in ip_list:
        count += 1
        print('Checking IP: ', ip)
        p = {'apikey': api, 'ip': ip}
        r = requests.get(u, p)
        results.append(r.json())
        if count == limit:
            print("you're using a free api key - this may take some time")
            time.sleep(65)
            print('ok, back to work....')
            count = 0

    data = [['ip', 'owner', 'country', '#_detected_urls']]
    c = 0
    t = len(ip_list)

    # Parses json responses from VirusTotal
    for i in results:
        if 'as_owner' in i :
            as_owner = i['as_owner']
        else:
            as_owner = 'none'
        if 'country' in i:
            country = i["country"]
        else:
            country = 'none'
        ip = ip_list[c]
        detected_urls = i['detected_urls']

        num_of_detections = 0
        for d in detected_urls:
            num_of_detections += 1
        data.append([ip, as_owner, country, num_of_detections])
        c += 1
    return data





def vt_results():
    data = vt_caller()
    # creates a dataframe of results
    df = pd.DataFrame(data)

    print("Here's your Data, a CSV has also been created name ipvtresults.csv")

    for i in data:
        print(i)

    # Creates a csv of results
    mt = dt.datetime.now()
    ft = str(mt.strftime('%H-%M-%S-%f'))
    outfile = 'ip_vtresults-' + ft + '.csv'
    output = df.to_csv(outfile)
    return output

print("** Welcome to the Virustotal Checker for free API Keys!!** \n")
intake_file(file_name)

vt_results()
