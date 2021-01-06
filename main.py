import requests
import argparse
import apic_login
import mso_login
import interface_description

# Supress HTTPS Warnings
requests.urllib3.disable_warnings()

apic=None
mso=None
username=None
password=None


if __name__ == "__main__":
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description='Common ACI Functions'
    )
    # Add the parameters positional/optional
    parser.add_argument('-a', '--apic', help='IP Address or hostname of APIC', default=apic, metavar='')
    parser.add_argument('-m', '--mso', help='IP Address or hostname of MSO', metavar='', default=None)
    parser.add_argument('-u', '--username', help='Username for APIC', default=username, metavar='')
    parser.add_argument('-p', '--password', help='Password for APIC', default=password, metavar='')
    parser.add_argument('--add-epg', help='Create an EPG on an APIC', metavar='')
    parser.add_argument('--interface-description', help='Add and interface description an APIC', action='store_true')
    # Parse the arguements
    command_line_args = parser.parse_args()
    args = vars(command_line_args)

    # Log into APIC
    if args['apic'] is not None and args['username'] is not None\
    and args['password'] is not None and args['mso'] is None:
        session = apic_login.apic_login(**args)
        args['session'] = session
        # Run interface description code
        if command_line_args.interface_description is True:
        	interface_description.main(**args)


    # Log into MSO    
    if args['mso'] is not None and args['username'] is not None\
    and args['password'] is not None:
        session = mso_login.mso_login(**args)
