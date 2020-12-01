#######################################################################################################################################
# Title: Meraki CLI Tools
# Author: Tory Davenport
# Date Started: 2/20/2019
# Description: This is a collection of functions written to interface with the Meraki dashboard API to simplify administrative tasks.
#######################################################################################################################################

# Import Statements
import csv
import os
from os import system, name 
import datetime
from meraki import meraki
import time
from time import sleep
import getpass
import json 

current_date_time = str(datetime.datetime.now())
organization_id = "null"
api_key = "093b24e85df15a3e66f1fc359f4c48493eaa1b73"
	
organization_id = 0
suppress_print = True

###########################################################################################################################
# DEFINE CLASSES																										  #
###########################################################################################################################

# Defines an organization as object
class Organization:
	# Initializer / Instance Attributes	
	def __init__(self, name, org_id):
		self.name = name
		self.org_id = org_id
	
	# Function can be called to pull the organization list using the specified api_key, format the data and generate a report.
	def get( api_key, suppress_print, current_date_time ):
		report_path = f"./Reports/Organization_Report.txt"
		data = meraki.myorgaccess(api_key, suppress_print)
		org_data = json.dumps(data,indent=4)
		org_length = len(meraki.myorgaccess(api_key, suppress_print))
		print(f"You have {org_length} organizations")
				
		print_report(org_data, report_path)
		return print(f"\nA copy of of this data has been stored in {report_path}")
	
	def add( api_key, new_organization_name ):
		# Put variables into place and execute command
		meraki.addorg(api_key, new_organization_name, suppress_print)
		print("Success! " + new_organization_name + " has been added!")
		input("\nPress any key to continue. . .")
		return

# Defines an Administrator as object
class Admin:
		
	# Initializer / Instance Attributes	
	def __init__(self, name, email, admin_id, networks, tags, two_fa, last_active, account_status, has_api_key, org_access):
		self.name = name
		self.email = email
		self.admin_id = admin_id
		self.networks = networks
		self.tags = tags
		self.two_fa = two_fa
		self.last_active = last_active
		self.account_status = account_status
		self.has_api_key = has_api_key
		self.org_access = org_access

	# Function can be called to pull the admin list using the specified api_key and org id, format the data and generate a report.
	def get( organization_id, suppress_print, current_date_time ):
		report_path = f"./Reports/Admin_Report_{organization_id}.txt"
		data = meraki.getorgadmins(api_key, organization_id, suppress_print)
		admin_data = json.dumps(data,indent=4)
		admin_length = len(admin_data)
		
		print(f"\nYou have {admin_length} admins in organization number {organization_id}")
		data = json.dumps(admin_data, indent=4)
		print_report(data, report_path)
		return print(f"\nA copy of of this data has been stored in {report_path}")

	def add_admins( api_key, organization_id ):
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
			org_access = input("Enter access level (full, read-only, none): ")
			print()
			meraki.addadmin(api_key, organization_id, email, name, org_access)
			counter = counter + 1
			print()
			print ("Success! " + name + " has been granted " + org_access + " access to organization ID " + organization_id)
		input("\nPress any key to continue. . .")
		clear()

	def add_admins_all_organizations( api_key, suppress_print, org_length, org_data ):
		clear()
		input("\nVERY IMPORTANT NOTE: In order for this bulk add script to work correctly, you need at add your admin to one organization and they will\n"
			"need to first accept the access and create their password on one organization before you can bulk add them to the rest.\n"
			"This is a limitation of the meraki dashboard api. Please use the add admin to one organization option, add your admin to one, then \n"
			"Use this script to bulk add them to the rest.\nYou must type their name and email exactly as you did for the first organization.\n"
			"Press enter to continue ...")

		org_length = org_length
		org_data = org_data

		name = input("Enter the Admins First and Last name: ")
		email = input("Enter the Admins email address: ")
		org_access = input("Enter access level (full, read-only, none): ")
		
		for item in range(org_length):
			# Take list data and create a dictionary with key-pair values
			organization_list = org_data[item]
			organization_id = organization_list['id']
			meraki.addadmin(api_key, str(organization_id), email, name, org_access)
			print(f"You have successfully added {name} to {organization_list['name']}")
			

	def delete( api_key, organization_id, query ):
		
		admin_data = meraki.getorgadmins(api_key, organization_id, suppress_print)
		admin_length = len(admin_data)
		counter = 1
		
		for item in range(admin_length):
			parser = list(admin_data[item].values())
			entry_0 = str(parser[0])
			entry_1 = str(parser[1])
			entry_2 = str(parser[2])
			
			if entry_1 == query:
				print(f"\n! Removing {entry_0}.. from organization # {organization_id} ")
				meraki.deladmin(api_key, organization_id, entry_2)
			

		"""input("Warning: This admin is about to be deleted.. Press enter to accept)")
								meraki.deladmin(api_key, organization_id, admin_id)"""
		#clear()
		return

	def delete_admin_all_organizations( api_key, org_length, org_data, query ):
		org_length = org_length
		org_data = org_data
		for item in range(org_length):
			organization_list = org_data[item]
			organization_id = organization_list['id']
			Admin.delete( api_key, organization_id, query )


	def get_admins_all_organizations( api_key, suppress_print, org_length, org_data ):
		org_length = org_length
		org_data = org_data
		for item in range(org_length):
			# Take list data and create a dictionary with key-pair values
			organization_list = org_data[item]
			organization_id = organization_list['id']
			Admin.get( organization_id, suppress_print, current_date_time )


###########################################################################################################################
# DEFINE FUNCTIONS																										  #
###########################################################################################################################
# Define a method for clearing the terminal
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

"""Function for generating reports printwith a custom file name -- Data flows from the function it is generated in, passed to 
   print_report and a formatted test file report is created with a custom file name."""
def print_report( data, report_path ):
	path = "./Reports/"
	directory_exsists = (os.path.isdir(path))
	
	if directory_exsists == True:	
		with open(report_path,'a', encoding = 'utf-8') as file:
			file.write(data)
			file.close()
	else:
		print("Creating Directory..")
		try:
			os.mkdir(path)
		except OSError:
			print("The directory creation has failed.")

def print_object( pass_object ):
	object_ = pass_object
	for attr, value in object_.__dict__.items():
			print(attr, value)
			print()

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

# Define menus below
def admin_menu_loop():
	clear()
	running = True
	while running == True:
		print("Please make a selection: ")
		print("\n1: Add one or more admin(s) to one organization") 
		print("2: Bulk Add an admin to all organizations")
		print("3: Delete an admin")
		print("4: Delete admin from all organizations\n")
		choice = input("Please make a choice or type 'back' to exit to the previous menu: ")
		if choice == "1":
			organization_id = input("Please enter an organization ID number: ")
			Admin.add_admins(api_key, organization_id)
		elif choice == "2":
			Admin.add_admins_all_organizations( api_key, suppress_print, org_length, org_data )
		elif choice == "3":
			clear()
			organization_id = input("Enter the Organization ID number: ")
			query = input("Please enter the email of the person you wish to remove: ")
			Admin.delete(api_key, organization_id, query)
		elif choice == "4":
			clear()
			query = input("Please enter the email of the person you wish to remove: ")
			Admin.delete_admin_all_organizations(api_key, org_length, org_data, query)
		elif choice == "back":
			clear()
			return
		else:
			clear()
			print("Invalid Option, Try again!\n")

def reports_menu_loop():
	clear()
	running = True
	while running == True:
		print("Please make a selection: ")
		print("\n1: Run Organization Report") 
		print("2: Run Admin Report for a specific organization")
		print("3: Run Admin Report for every organization attached to this API Key")
		
		choice = input("\nPlease make a choice or type 'back' to exit to the previous menu: ")
		
		if choice == "1":
			clear()
			Organization.get(api_key, suppress_print, current_date_time, org_length, org_data)
			input("\nPress enter to continue")
			clear()
		elif choice == "2":
			clear()
			organization_id = input("Please enter organization ID#: ")
			Admin.get( organization_id, suppress_print, current_date_time )
			input("\nPress enter to continue")
			clear()
		elif choice == "3":
			clear()
			Admin.get_admins_all_organizations( api_key, suppress_print, org_length, org_data )
			input("\nPress enter to continue")
			clear()
		elif choice == "back":
			clear()
			return
		else:
			clear()
			print("Invalid Option, Try again!\n")

def organization_menu_loop():
	clear()
	running = True
	while running == True:
		print("Please make a selection: ")
		print("\n1: Add an organization") 
		print("2: ")
		print("3: ")
		
		choice = input("\nPlease make a choice or type 'back' to exit to the previous menu: ")
		
		if choice == "1":
			clear()
			input("Please enter the name of the organization you are creating: ")
			Organization.add( api_key, new_organization_name )
		elif choice == "2":
			pass
		elif choice == "3":
			pass
		elif choice == "back":
			clear()
			return
		else:
			clear()
			print("Invalid Option, Try again!\n")

def main_loop():
	clear()
	running = True
	while running == True:
		print("Welcome to Meraki CLI Tools\n" + "Please make a selection: \n")
		print("1: Reporting/Information Gathering ") 
		print("2: Manage Admins")
		print("3: Manage Organizations")
		
		choice = input("\nPlease make a choice or type 'quit' to exit program: ")

		if choice == "1":
			clear()
			reports_menu_loop()

		elif choice == "2":
			clear()
			admin_menu_loop()

		elif choice == "3":
			clear()
			organization_menu_loop()

		elif choice == "4":
			pass
		elif choice == "5":
			pass
			
		elif choice == "6":
			pass
			
		elif choice == "7":
			pass
			
		elif choice == "8":
			pass
			
		elif choice == "quit":
			clear()
			print("The program is now shutting down. . .")
			sleep(2)
			clear()
			exit()

		else:
			clear()
			print("Invalid Option, Try again!\n")

###########################################################################################################################
# FUNCTION CALLS																										  #
###########################################################################################################################

clear()
#main_loop()
Admin.get( '578149602163688717', suppress_print, current_date_time )
