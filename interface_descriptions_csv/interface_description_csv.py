import requests
import json
import time
import getpass
import urllib3
import re
import csv

username = 'admin'
#password = 'PASSWORD'
password = getpass.getpass()

### Update this IP Address
### Update this IP Address
apic = '10.5.9.11'
### Update this IP Address
### Update this IP Address

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


def interface_format(interface_id):
    '''
    Format Interface ID as needed
    '''
    pattern = re.compile('^\d+\/\d+$')
    match = pattern.match(interface_id)
    if not match:
        print("Invalid Interface Format")
        quit()
    else:
        pass
    interface_split = []
    interface_split.append(interface_id.split('/'))
    interface_underscore = str(interface_split[0][0]) + '_' + str(interface_split[0][1])
    return interface_underscore

def set_interface_description(session, apic, node_id, interface_id, interface_description):
    '''
    Set interface description
    '''
    interface_underscore = interface_format(interface_id)
    url = 'https://' + apic + '/api/node/mo/uni/infra/hpaths-' + node_id + '_eth' + interface_underscore + '.json'
    json = {"infraHPathS":{"attributes":{"rn":"hpaths-" + str(node_id) + "_eth" + interface_underscore + "","dn":"uni/infra/hpaths-" + str(node_id) + "_eth" + interface_underscore + "","descr":"" + interface_description + "","name":"" + str(node_id) + "_eth" + interface_underscore + ""},"children":[{"infraRsHPathAtt":{"attributes":{"dn":"uni/infra/hpaths-" + str(node_id) + "_eth" + interface_underscore + "/rsHPathAtt-[topology/pod-1/paths-" + node_id + "/pathep-[eth" + interface_id + "]]","tDn":"topology/pod-1/paths-" + node_id + "/pathep-[eth" + interface_id + "]"}}}]}}
    response = session.post(url, json=json, verify=False)
    print(response)


session = login()

with open('interfaces.csv') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        set_interface_description(session, apic=apic, node_id=row[0], interface_id=row[1], interface_description=row[2])
