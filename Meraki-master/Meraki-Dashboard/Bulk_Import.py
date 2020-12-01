#############################################################################
# Description: This script is simplified for bulk adding admins to the Meraki.
#              Adapted from Meraki_tools.py, This will allow using a data structure
#              to import the names of admins while the Meraki_tools.py script will
#			   not.
# 
# Written by Tory Davenport
# Last Update 7/11/2019
#
#
#############################################################################

############################################################################
#                          Import Statements                               #
############################################################################
from meraki import meraki
import getpass
import json
from time import sleep

############################################################################
#                          Global Variables                                #
############################################################################
api_key = getpass.getpass(prompt='Please enter your Meraki API KEY to begin:')
suppress_print = False
organization_id = "null"

# Generate a list of organizations to reference later and get the length (How many)
try:
	org_data = meraki.myorgaccess(api_key, suppress_print) 
	org_length = len(org_data)
except TypeError:
	exit("ERROR: This is not a valid API Key, please reload and try again")

############################################################################
#                           Put your admins in this list                   #
############################################################################

admins = {"Name0" : "REDACTED", "Email0" : "REDACTED", "Perm0" : "Full" } 

list_length = len(admins)
num_admins = (list_length / 2)
def add_all_organizations(num_admins, list_length):
	try:
		for item in range(list_length):
			name = admins[f"Name{item}"]
			email = admins[f"Email{item}"]
			access = admins[f"Perm{item}"]
			for item in range(org_length):
				organization_list = org_data[item]
				organization_id = organization_list['id']
				organization_name = organization_list['name']
				#meraki.addadmin(api_key, str(organization_id), email, name, access)
				print(f"\nAdding {name} to organization {organization_name} with {access} privledges")
	except KeyError:
		print("All Admins Parsed")
		pass	


def add_all_to_single(num_admins, list_length):
	print(f"There are {num_admins} in the database")
	organization_id = input("org-id-number> ")
	try:
		for item in range(list_length):
			name = admins[f"Name{item}"]
			email = admins[f"Email{item}"]
			access = "full"
			print(meraki.addadmin(api_key, str(organization_id), email, name, access))
			print(f"\nAdding {name} to organization {organization_id} with full privledges")

	except KeyError:
		print("All Admins Parsed")
		pass		

#add_all_organizations(num_admins, list_length)
add_all_to_single(num_admins, list_length)
	
