#############################################################################
# Description: This tool will pull admin information from every organization
# 			   to compare against a known list of admins we need to make sure
#              have access and will return a file showing the differences.
# Written by Tory Davenport
# Last Update 7/15/2019
#############################################################################

############################################################################
#                          Import Statements                               #
############################################################################
from meraki import meraki
import getpass
import json
from time import sleep
from pathlib import Path
############################################################################
#                          Global Variables                                #
############################################################################
api_key = getpass.getpass(prompt='Please enter your Meraki API KEY to begin: ')
suppress_print = False
organization_id = None
access = "full"
filename = None
# Generate a list of organizations to reference later and get the length (How many)
try:
	org_data = meraki.myorgaccess(api_key, suppress_print) 
	org_length = len(org_data)
except TypeError:
	exit("ERROR: This is not a valid API Key, please reload and try again")

try:
	for item in range(org_length):
		organization_list = org_data[item]
		organization_id = organization_list['id']
		organization_name = organization_list['name']
		output = meraki.getorgadmins(api_key, organization_id, suppress_print)
		filename = f"{organization_name}_Admins.txt"
		report_path = Path(f"./Reports/Diff/{organization_name}.txt")
		with open(report_path, 'w', encoding = 'utf-8') as file:
			file.write(f"Organization:{organization_name}\n{json.dumps(output, indent=4)}")
except Exception as e:
	raise e