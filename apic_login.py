import requests
import getpass

# Supress HTTPS Warnings
requests.urllib3.disable_warnings()


def main():
    '''
    Manually prompt the user for login information
    '''
    args = {}
    args['apic'] = str(input('APIC: '))
    args['username'] = str(input('Username: '))
    args['password'] = str(getpass.getpass(prompt='Password: '))
    args['session'] = apic_login(**args)
    return args


def apic_login(**kwargs):
    '''
    Log into APIC and return session
    '''
    url = 'https://' + kwargs['apic'] + '/api/aaaLogin.json'
    payload = {'aaaUser':{'attributes':{'name':kwargs['username'],'pwd':kwargs['password']}}}
    session = requests.Session()
    response = session.post(url, json=payload, verify=False)
    return session


if __name__ == "__main__":
    try:
        print(main())
    except KeyboardInterrupt:
        pass
