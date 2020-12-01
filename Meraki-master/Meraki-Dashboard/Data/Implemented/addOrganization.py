# Written by Tory Davenport
# Description: Add a new organization
# Last Updated: 2/4/2019

from meraki import meraki

def addOrganization( apiKey, suppressPrint ):
	clear()
	# Add Organization ID
	newOrganizationName = input("Enter a name for the new organization: ")
	# Put variables into place and execute command
	meraki.addorg(apiKey, newOrganizationName, suppressPrint)
	print("Success! " + organizationName + " has been added!\nDetails:")
	return

