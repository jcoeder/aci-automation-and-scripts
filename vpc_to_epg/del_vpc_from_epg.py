import requests
import json
import time
import getpass
import urllib3
import re

username = 'admin'
password = 'HAHAHA'
#password = getpass.getpass()

### Update this IP Address
### Update this IP Address
apic = '10.25.1.11'
### Update this IP Address
### Update this IP Address

# Disable SSL Warnings
urllib3.disable_warnings()

epgs = {'EPG-NAME1': '1915',
        'EPG-NAME2': '1935',
        'EPG-NAME3': '1932',
        'EPG-NAME4': '1931',
        }

def login():
    '''
    Log into APIC and return session
    '''
    url = 'https://' + apic + '/api/aaaLogin.json'
    payload = {'aaaUser':{'attributes':{'name':username,'pwd':password}}}
    session = requests.Session()
    response = session.post(url, json=payload, verify=False)
    return session

def del_vpc_from_epgs_1(session, apic=apic, epgs=epgs):
    '''
    4 Different functions because its easier than looking up the protpath of the VPC name
    '''
    for key, value in epgs.items():
        url = 'https://' + apic + '/api/node/mo/uni/tn-TENANT_NAME/ap-AP_NAME/epg-' + key +'/rspathAtt-[topology/pod-1/protpaths-201-202/pathep-[IPG_NAME]].json'
        json = {"fvRsPathAtt":{"attributes":{"dn":"uni/tn-TENANT_NAME/ap-AP_NAME/epg-" + key + "/rspathAtt-[topology/pod-1/protpaths-201-202/pathep-[IPG_NAME]]","status":"deleted"},"children":[]}}
        response = session.post(url, json=json, verify=False)
        print(response)

def del_vpc_from_epgs_2(session, apic=apic, epgs=epgs):
    '''
    4 Different functions because its easier than looking up the protpath of the VPC name
    '''
    for key, value in epgs.items():
        url = 'https://' + apic + '/api/node/mo/uni/tn-TENANT_NAME/ap-AP_NAME/epg-' + key +'/rspathAtt-[topology/pod-1/protpaths-201-202/pathep-[IPG_NAME]].json'
        json = {"fvRsPathAtt":{"attributes":{"dn":"uni/tn-TENANT_NAME/ap-AP_NAME/epg-" + key + "/rspathAtt-[topology/pod-1/protpaths-201-202/pathep-[IPG_NAME]]","status":"deleted"},"children":[]}}
        response = session.post(url, json=json, verify=False)
        print(response)

			
session = login()
del_vpc_from_epgs_1(session, apic, epgs)
del_vpc_from_epgs_2(session, apic, epgs)
