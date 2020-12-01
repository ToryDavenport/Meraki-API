"""
Written by Tory Davenport
Date Started: 2/20/2019

Description: Creating a class to simplify admin operations dealing with their properties
"""
import csv
import os
from os import system, name 
import datetime
from meraki import meraki
import time
from time import sleep
import getpass

current_date_time = str(datetime.datetime.now())
api_key = "093b24e85df15a3e66f1fc359f4c48493eaa1b73"
organization_id = "578149602163688717"
suppress_print = False

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
		org_data = meraki.myorgaccess(api_key, suppress_print) 
		org_length = len(org_data)
		#report_path = f"./Reports/Organization_Report_{current_date_time}.txt"
		header = f"You have {org_length} organizations"
		print(header)
		for item in range(org_length):
			# Take list data and create a dictionary with key-pair values
			organization_list = org_data[item]
			# Access values
			name = organization_list['name']
			org_id = organization_list['id']		
			# Create as object	
			organization = Organization(name, org_id)
			# Generate Data
			data = (f"""\nOrganization Name: {organization.name}\nOrganization ID: {organization.org_id}""")
			# Generate report
			#print_report(data, report_path)
			print(data)
	
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
	def get( api_key, organization_id, suppress_print, current_date_time ):
		#report_path = f"./Reports/Admin_Report_{current_date_time}.txt"
		admin_data = meraki.getorgadmins(api_key, organization_id, suppress_print)
		admin_length = len(admin_data) 
		header = f"""You have {admin_length} admins for organization {organization_id}:\n """
		print(header)
		for item in range(admin_length):
			# Take list data and create a dictionary with key-pair values
			admin_list = admin_data[item]
			# Access values
			name = admin_list['name']
			email = admin_list['email']
			admin_id = admin_list['id']
			networks = admin_list['networks']
			tags = admin_list['tags']
			two_fa = admin_list['twoFactorAuthEnabled']
			last_active = admin_list['lastActive']
			account_status = admin_list['accountStatus']
			has_api_key = admin_list['hasApiKey']
			org_access = admin_list['orgAccess']
			# Create as object	
			admin = Admin(name, email, admin_id, networks, tags, two_fa, last_active, account_status, has_api_key, org_access)
			# Generate Data
			data = (f"""\nName: {admin.name}\n\tEmail: {admin.email}\n\tAdmin ID: {admin.admin_id}\n\tNetworks: {admin.networks}\n\tTags: {admin.tags}\n\t2FA Enabled: {admin.two_fa}\n\tLast Active: {admin.last_active} \n\tAccount Status: {admin.account_status} \n\tHas API Key: {admin.has_api_key} \n\tOrganization Access Level: {admin.org_access}""")
			# Generate report
			#print_report(data, report_path)
			print(data)

	def add_single( api_key, organization_id, email, name, org_access ):
		# Put variables into place and execute command
		meraki.addadmin(api_key, organization_id, email, name, org_access)
		print ("Success! " + name + " has been granted " + org_access + " access to organization ID " + organization_id)
		input("\nPress any key to continue. . .")

	def delete_single( api_key, organization_id, admin_id ):
		input("Warning: This admin is about to be deleted.. Press enter to accept)")
		meraki.deladmin(api_key, organization_id, admin_id)
		return


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

"""Function for generating reports with a custom file name -- Data flows from the function it is generated in, passed to 
   print_report and a formatted test file report is created with a custom file name."""
def print_report( data, report_path ):
	path = "./Reports/"
	directory_exsists = (os.path.isdir(path))
	
	if directory_exsists == True:	
		with open(report_path,'a', encoding = 'utf-8') as file:
			file.write(data)
		#print(data)
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

###########################################################################################################################
# FUNCTION CALLS																										  #
###########################################################################################################################
