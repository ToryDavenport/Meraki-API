from meraki import meraki
from os import system, name 
import time
from time import sleep
import getpass


#meraki.getorgadmins(api_key,organization_id,suppress_print)

#print(meraki.deladmin(apiKey, organizationID, adminID))




def admin_report_all( api_key, organization_database_length ):
	for item in range(organization_database_length):
		# Enter organization ID to begin operation
		organization_id = organization_id_number_list[item]
		organization_name = organization_names_list[item]
		# New admin variables
		admin_report( api_key, organization_id, organization_name, suppress_print )
	return 
	input("\nPress any key to continue. . .")
	clear()
def generate_org_id_list( api_key, organization_database, organization_database_length ):
	# Iterate throught he list and extract the data. Output clean data
	for item in range(organization_database_length):
		# Convert the dictionary values to a list
		organization_list = list(organization_database[item].values())
		# Select the Organization ID and Name, adding them to the list
		organization_id_number = str(organization_list[0])
		organization_name = str(organization_list[1])
		organization_names_list.append(organization_name)
		organization_id_number_list.append(organization_id_number)
	return
def get_api_key():
	# Take in API key securely, held in variable until program terminates
	key = getpass.getpass(prompt='Please enter your Meraki API KEY: ')
	return (key)

def get_all_organizations( api_key, suppress_print ):
	# Pull json from meraki into a list (Store in RAM only)
	organizations = meraki.myorgaccess(api_key, suppress_print)
	return (organizations)

def measure( data ):
	data_length = len(data)
	return (data_length)
def admin_report( api_key, organization_id, organization_name, suppress_print ):
	#clear()
	# GET list of admins
	admins_list = meraki.getorgadmins(api_key,organization_id,suppress_print)
	# Find the length of the list
	admins_list_length = measure( admins_list )
	print("Here is the list of admins for organization name:","'"+organization_name+"',", "ID #:",organization_id)
		# Iterate throught he list and extract the data. Output clean data
	for item in range(admins_list_length):
		# Convert the dictionary values to a list
		admin_list = list(admins_list[item].values())
		# Select the Admin Name
		admin_name = str(admin_list[0])
		# Select the Admin's Email
		admin_email = str(admin_list[1])
		# Select the Admin ID to print
		admin_id = str(admin_list[2])
		# Select the Two-Factor Auth.
		admin_two_factor_auth = str(admin_list[5])
		# Select Last Active
		admin_last_active = str(admin_list[6])
		# Select account status
		admin_account_status = str(admin_list[7])
		# Select Organization Access Level
		admin_organization_level = str(admin_list[8])
		# Print Values
		print("\nName: " + admin_name, "\nEmail: " + admin_email, "\nAdmin ID #: " + admin_id, "\nTwo-Factor Authentication: " + admin_two_factor_auth, "\nLast Active: " + admin_last_active, "\nAccount status: " + admin_account_status, "\nOrganization Access Level: " + admin_organization_level)
	#time.sleep(1)
	input("\nPress any key to continue. . .")
	clear()
	return

def adminbulk_printer ( data, data_length, organization_id, query ):
	counter = 0
	for item in range(data_length):
		counter = counter + 1
		parser = list(data[item].values())
		entry_0 = str(parser[0])#Admin Name
		entry_1 = str(parser[1])#Admin Email
		entry_2 = str(parser[2])#Admin ID #
		if entry_1 == query:	
			print("Match: ", data[item])
			#meraki.deladmin(api_key, organization_id, entry_2)
	return

def delete_admin_bulk():
	query = input("Please enter the email of the person you want to remove: ")
	for item in range(organization_database_length):
		organization_id = organization_id_number_list[item]
		admin_data = meraki.getorgadmins(api_key,organization_id,suppress_print)
		admin_length = measure(admin_data)
		print("organization: ", organization_id)
		adminbulk_printer( admin_data, admin_length, organization_id, query )
	return

# Set Variables
suppress_print = "True"
api_key = "Default_Key"
organization_id = "default organization id"
organization_name = "default organization name"
organization_id_number_list = []
organization_names_list = []
api_key = "093b24e85df15a3e66f1fc359f4c48493eaa1b73"#get_api_key()
organization_database = get_all_organizations( api_key, suppress_print )
organization_database_length = measure( organization_database )


#print(type(get_all_organizations( api_key, suppress_print )))
generate_org_id_list( api_key, organization_database, organization_database_length )
delete_admin_bulk()

