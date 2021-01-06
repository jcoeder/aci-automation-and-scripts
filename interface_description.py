import requests
import re
import json
import apic_login

# Supress HTTPS Warnings
requests.urllib3.disable_warnings()

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


def print_interface_information(**kwargs):
    '''
    Print interface information to user
    '''
    url = "https://" + kwargs['apic'] + "/api/node/mo/topology/pod-1/node-"+ kwargs['node_id'] + "/sys/phys-[eth" + kwargs['interface_id'] + "].json?&rsp-subtree-include=relations"
    response = kwargs['session'].get(url, verify=False)
    json_string = response.text
    interface_information = json.loads(json_string)
    print(interface_information['imdata'][7]['l1PhysIf']['attributes']['id'])
    print(interface_information['imdata'][7]['l1PhysIf']['attributes']['descr'])


def main(**kwargs):
    '''
    Add a description to a physical interface in the APIC
    '''
    kwargs['node_id'] = str(input('Node ID (Ex: 101): '))
    kwargs['interface_id'] = str(input('Interface ID (Ex: "1/1"): '))
    kwargs['interface_description'] = str(input('Interface Description: '))
    kwargs['interface_underscore'] = interface_format(kwargs['interface_id'])
    url = 'https://' + kwargs['apic'] + '/api/node/mo/uni/infra/hpaths-' + kwargs['node_id'] + '_eth' + kwargs['interface_underscore'] + '.json'
    json = {"infraHPathS":{"attributes":{"rn":"hpaths-" + str(kwargs['node_id']) + "_eth" + kwargs['interface_underscore'] + "","dn":"uni/infra/hpaths-" + str(kwargs['node_id']) + "_eth" + kwargs['interface_underscore'] + "","descr":"" + kwargs['interface_description'] + "","name":"" + str(kwargs['node_id']) + "_eth" + kwargs['interface_underscore'] + ""},"children":[{"infraRsHPathAtt":{"attributes":{"dn":"uni/infra/hpaths-" + str(kwargs['node_id']) + "_eth" + kwargs['interface_underscore'] + "/rsHPathAtt-[topology/pod-1/paths-" + kwargs['node_id'] + "/pathep-[eth" + kwargs['interface_id'] + "]]","tDn":"topology/pod-1/paths-" + kwargs['node_id'] + "/pathep-[eth" + kwargs['interface_id'] + "]"}}}]}}
    response = kwargs['session'].post(url, json=json, verify=False)
    print_interface_information(**kwargs)

if __name__ == "__main__":
    try:
        main(**apic_login.main())
    except KeyboardInterrupt:
        pass
