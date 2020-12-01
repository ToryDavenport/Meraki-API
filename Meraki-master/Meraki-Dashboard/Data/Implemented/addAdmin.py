# Written by Tory Davenport
# Description: Add admins to an organization (Allow single mode and bulk edit)
# Last Updated: 2/4/2019

from meraki import meraki

# Add API Key
apiKey = input("Please enter your API Key: ")
# Add Organization ID
organizationID = input("Enter an organization ID: ")
# New admin variables
name = input("Enter the Admins First and Last name: ")
email = input("Enter the Admins email address: ")
organizationAccessLevel = input("Enter access level (full, read-only, none): ")

# Put variables into place and execute command to add admin

print(meraki.addadmin(apiKey, organizationID, email, name, organizationAccessLevel))						
