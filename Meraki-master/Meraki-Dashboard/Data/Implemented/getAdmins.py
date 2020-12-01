# Written by Tory Davenport
# Description: This script returns a list of admins for a given organization
# Last Updated: 2/4/2019

# Import meraki

from meraki import meraki

# Create variables
apiKey = input("Please enter your API Key: ")
# Add organization ID
organizationID = input("Enter an organization ID: ")

adminDatabase = (meraki.getorgadmins(apiKey, organizationID))
adminDatabaseLength = (len(adminDatabase))

print("You have", adminDatabaseLength, "admin(s)")
print()

# Display a list to the user
for i in range(adminDatabaseLengthitem):
	print (i, adminDatabase[i])
	print()

exit()

