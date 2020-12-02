import requests
import json
import time
import getpass
import urllib3
import re

username = 'admin'
#password = 'PASSWORD'
password = getpass.getpass()

### Update this IP Address
### Update this IP Address
apic = '10.11.1.11'
### Update this IP Address
### Update this IP Address

epg_id = str(input('Ex: EPG-NAME: '))
vlan_id = str(input('Ex: 1337: '))

# Disable SSL Warnings
urllib3.disable_warnings()


def login():
    '''
    Log into APIC and return session
    '''
    url = 'https://' + apic + '/api/aaaLogin.json'
    payload = {'aaaUser':{'attributes':{'name':username,'pwd':password}}}
    session = requests.Session()
    response = session.post(url, json=payload, verify=False)
    return session

def add_vpc_to_epg_1(session, apic=apic, epg_id=epg_id, vlan_id=vlan_id):
	'''
	4 Different functions because its easier than looking up the protpath of the VPC name
	'''
    url  = 'https://' + apic + '/api/node/mo/uni/tn-TENANT_NAME/ap-AP_NAME/epg-' + epg_id +'.json'
    json = {"fvRsPathAtt":{"attributes":{"encap":"vlan-" + vlan_id + "","instrImedcy":"immediate","tDn":"topology/pod-1/protpaths-205-206/pathep-[VPC_VPC1_NAME]","status":"created"},"children":[]}}
    response = session.post(url, json=json, verify=False)
    print(response)

def add_vpc_to_epg_2(session, apic=apic, epg_id=epg_id, vlan_id=vlan_id):
	'''
	4 Different functions because its easier than looking up the protpath of the VPC name
	'''
    url  = 'https://' + apic + '/api/node/mo/uni/tn-TENANT_NAME/ap-AP_NAME/epg-' + epg_id +'.json'
    json = {"fvRsPathAtt":{"attributes":{"encap":"vlan-" + vlan_id + "","instrImedcy":"immediate","tDn":"topology/pod-1/protpaths-205-206/pathep-[VPC_VPC2_NAME]","status":"created"},"children":[]}}
    response = session.post(url, json=json, verify=False)
    print(response)

def add_vpc_to_epg_3(session, apic=apic, epg_id=epg_id, vlan_id=vlan_id):
	'''
	4 Different functions because its easier than looking up the protpath of the VPC name
	'''
    url  = 'https://' + apic + '/api/node/mo/uni/tn-TENANT_NAME/ap-AP_NAME/epg-' + epg_id +'.json'
    json = {"fvRsPathAtt":{"attributes":{"encap":"vlan-" + vlan_id + "","instrImedcy":"immediate","tDn":"topology/pod-1/protpaths-203-204/pathep-[VPC_VPC3_NAME]","status":"created"},"children":[]}}
    response = session.post(url, json=json, verify=False)
    print(response)

def add_vpc_to_epg_4(session, apic=apic, epg_id=epg_id, vlan_id=vlan_id):
	'''
	4 Different functions because its easier than looking up the protpath of the VPC name
	'''
    url  = 'https://' + apic + '/api/node/mo/uni/tn-TENANT_NAME/ap-AP_NAME/epg-' + epg_id +'.json'
    json = {"fvRsPathAtt":{"attributes":{"encap":"vlan-" + vlan_id + "","instrImedcy":"immediate","tDn":"topology/pod-1/protpaths-203-204/pathep-[VPC_VPC4_NAME]","status":"created"},"children":[]}}
    response = session.post(url, json=json, verify=False)
    print(response)
			
session = login()
add_vpc_to_epg_1(session, apic, epg_id, vlan_id)
add_vpc_to_epg_2(session, apic, epg_id, vlan_id)
add_vpc_to_epg_3(session, apic, epg_id, vlan_id)
add_vpc_to_epg_4(session, apic, epg_id, vlan_id)
