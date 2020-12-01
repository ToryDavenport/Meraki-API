# Written by Tory Davenport
# Description: Add admins to an organization (Allow single mode and bulk edit)
# Last Updated: 2/4/2019

from meraki import meraki

# Add API Key
apiKey = input("Please enter your API Key: ")
# Add Organization ID
organizationID = input("Enter an organization ID: ")
# Specify admin by ADMIN ID
adminID = input("Enter an Admin ID: ")
# Saftey Warning
print(input("Warning: This admin is about to be deleted.. Press any key to accept or ctrl+C to cancel operation"))
# Put variables into place and execute command to add admin
print(meraki.deladmin(apiKey, organizationID, adminID))						
