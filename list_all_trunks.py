#!/usr/bin python
#script to pull all the trunks out of a Twilio account and store them in a list

import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#disable the https security warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ACCOUNT_SID = '{insert your Account SID here}'
ACCOUNT_TOKEN = '{insert your Account Token here}'
TWILIO_TRUNK_URL ='https://trunking.twilio.com/v1/Trunks'

def fetch_all_trunks():
    trunks = []
    trunks_url=TWILIO_TRUNK_URL
   
    while trunks_url is not None:
        print('\nGetting '+str(trunks_url)+'\n')
        r = requests.get( trunks_url, auth=(ACCOUNT_SID,ACCOUNT_TOKEN), verify=False)
        data = json.loads(r.text)
    
        for t in data['trunks']:
            print("Got trunk "+t["sid"]+" called "+t["friendly_name"])
            trunks.append(t)
        
        trunks_url = data["meta"]["next_page_url"]
        
    return trunks
        
    
trunks=fetch_all_trunks()  # all trunks in this Twilio account

    
  