import requests
import json
import pprint

from urllib3.exceptions import InsecureRequestWarning

apic = '10.29.1.11'
username = 'admin'
password = 'MEOW'

def login():
    auth_url = 'https://' + apic + '/api/aaaLogin.json'
    payload = {
        'aaaUser':{
           "attributes":{
             'name': username,
             'pwd': password
           }
        }
    }
    s = requests.session()
    s.post(auth_url, json=payload, verify=False)
    return s

s = login()

def DO_SOMETHING():
    url = 'A URL THAT DOES SOMETHING'
    data = s.get(url, verify=False)
    return(data.json())
   
DO_SOMETHING()
