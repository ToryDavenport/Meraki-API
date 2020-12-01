#######################################################################################################################################
# Title: Meraki CLI Tools
# Author: Tory Davenport
# Description: This is a collection of functions written to interface with the Meraki dashboard API to simplify administrative tasks.
#######################################################################################################################################

# IMPORT STATEMENTS
from meraki import meraki
from os import system, name 
import time
from time import sleep
import getpass

#######################################################################################################################################
# DEFINE ALL FUNCTIONS BELOW THIS LINE																								  #
#######################################################################################################################################
# Function adds the ability to clear the screen as desired
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Program Menu
def menu():
	clear()
	running = True
	while running == True:
		print("Welcome to Meraki CLI Tools\n" + "Please make a selection: \n")
		print("1: Run Admin Report for a specific organization") 
		print("2: Run Organization Report")
		print("3: Bulk add multiple admins to one organization") 
		print("4: Run Admin Report for every organazation attached to this API Key")
		print("5: Add A New Organization")
		print("6: Delete an admin")
		print("7: Delete admin from all organizations")
		print("8: Bulk Add an admin to all organizations")
		print()

		choice = input("Please make a choice or type 'quit' to exit program: ")

		if choice == "1":
			clear()
			organization_id = input("Please enter the organization ID: ")
			admin_report( api_key, organization_id, organization_name, suppress_print )
		elif choice == "2":
			clear()
			organization_report( api_key, suppress_print )
		elif choice == "3":
			clear()
			organization_id = input("Please enter the organization ID: ")
			bulk_add_single_organization( api_key, organization_id, suppress_print)
		elif choice == "4":
			clear()
			admin_report_all( api_key, organization_database_length )
		elif choice == "5":
			clear()
			add_single_organization( api_key, suppress_print )
		elif choice == "6":
			clear()
			organization_id = input("Please enter the organization ID: ")
			admin_id = input("Please enter the admins unique admin ID: ")
			delete_single_admin( api_key, organization_id, admin_id )
			exit()
		elif choice == "7":
			clear()
			delete_admin_bulk()			
			exit()
		elif choice == "8":
			clear()
			bulk_add_multiple_organizations( api_key, organization_database_length )
			exit()
		elif choice == "quit":
			clear()
			exit()
		else:
			clear()
			print("Invalid Option, Try again!\n")

# Using the list from getOrganizations.. create an organization report
def organization_report( api_key, suppress_print ):
	clear()
	#counter = 0
	print("There are", organization_database_length, "organization(s) availible.\n")
	data_printer( organization_database, organization_database_length, "Organization ID#", "Name" )
	input ("\nPress any key to continue. . .")
	clear()
	return 

# Function to get admin report for a particular organization
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

# Get a list of every admin for every organization attached to API Key
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

# To add multiple admins to one organization
def bulk_add_single_organization( api_key, organization_id, suppress_print ):
	# Specify the number of admins you wish to add
	number_of_admins = int(input("How many admins would you like to add? "))
	# Start count at 1 not 0
	counter = 1	
	# While admin number is lt or eq to count, do ... 
	while counter <= number_of_admins: 
		# Display admin number
		print("Admin Number:", counter)
		print()
		# New admin variables
		name = input("Enter the Admins First and Last name: ")
		email = input("Enter the Admins email address: ")
		organizationAccessLevel = input("Enter access level (full, read-only, none): ")
		print()
		print(meraki.addadmin(api_key, organization_id, email, name, organizationAccessLevel))
		counter = counter + 1
		print()
	input("\nPress any key to continue. . .")
	clear()
	return

# To add admin to all organizations tied to an API key
def bulk_add_multiple_organizations( api_key, organization_database_length ):
	organizations_conditional = str(input("Are you adding admins to all organizations listed under your API key?\nType yes or no: "))
	# Specify the number of admins you wish to add
	#amountOfAdmins = int(input("How many admins would you like to add? "))
	if organizations_conditional == 'yes':
		name = input("Enter the Admins First and Last name: ")
		email = input("Enter the Admins email address: ")
		organization_access_level = input("Enter access level (full, read-only, none): ")
		
		for item in range(organization_database_length):
			# Start count at 1 not 0
			# adminNumber = 1
			# Enter organization ID to begin operation
			organization_id = organization_id_number_list[item]
			print(organization_id)
			# New admin variables
			print()
			print(meraki.addadmin(api_key, organization_id, email, name, organization_access_level))

	else:
		print("pass")		

# Extract organization id numbers for all organizations 
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

def add_single_organization( api_key, suppress_print ):
	clear()
	# Add Organization ID
	new_organization_name = input("Enter a name for the new organization: ")
	# Put variables into place and execute command
	meraki.addorg(api_key, new_organization_name, suppress_print)
	clear()
	print("Success! " + new_organization_name + " has been added!")
	input("\nPress any key to continue. . .")
	clear()
	return

def data_printer( data, data_length, entry_0_label, entry_1_label ):
	counter = 0
	for item in range(data_length):
		counter = counter + 1
		parser = list(data[item].values())
		entry_0 = str(parser[0])
		entry_1 = str(parser[1])
		print(counter, ".", entry_0_label, ":", entry_0, entry_1_label, ":", entry_1)
		print()
	return 

def admin_delete_bulk_printer( data, data_length, organization_id, query ):
	counter = 0
	for item in range(data_length):
		counter = counter + 1
		parser = list(data[item].values())
		entry_0 = str(parser[0])#Admin Name
		entry_1 = str(parser[1])#Admin Email
		entry_2 = str(parser[2])#Admin ID #
		if entry_1 == query:	
			print("\nMatch! Removing Admin.. ")
			meraki.deladmin(api_key, organization_id, entry_2)
	return

def delete_admin_bulk():
	query = input("Please enter the email of the person you want to remove: ")
	for item in range(organization_database_length):
		organization_id = organization_id_number_list[item]
		admin_data = meraki.getorgadmins(api_key,organization_id,suppress_print)
		admin_length = measure(admin_data)
		print("Checking for", query, "in organization #: ", organization_id)
		admin_delete_bulk_printer( admin_data, admin_length, organization_id, query )
	return

def get_api_key():
	# Take in API key securely, held in variable until program terminates
	key = getpass.getpass(prompt='Please enter your Meraki API KEY: ')
	return (key)

def get_all_organizations( api_key, suppress_print ):
	# Pull json from meraki into a list (Store in RAM only)
	organizations = meraki.myorgaccess(api_key, suppress_print)
	return (organizations)

def delete_single_admin( api_key, organization_id, admin_id ):
	input("Warning: This admin is about to be deleted.. Press enter to accept)")
	meraki.deladmin(api_key, organization_id, admin_id)
	return

def measure( data ):
	data_length = len(data)
	return (data_length)


########### BEGIN PROGRAM BODY ########################################################################################################
clear()
print("Welcome to Meraki Administrative Tasks. To use this software, you will need an API key for your organization.")
print("IMPORTANT NOTE: Your API key is unique to your dashboard and should be treated like a password\nAs such, you will not see input as you copy/paste or type in your key. ")
print("Your key will be held in memory for the duration of this session, however, it will not be stored after the program is terminated. Please store your key in a secure location.")
print()

# Set Variables
suppress_print = "True"
api_key = "Default_Key"
organization_id = "default organization id"
organization_name = "default organization name"
organization_id_number_list = []
organization_names_list = []
api_key = get_api_key()
organization_database = get_all_organizations( api_key, suppress_print )
organization_database_length = measure( organization_database )

# Start program
generate_org_id_list( api_key, organization_database, organization_database_length )
menu()




