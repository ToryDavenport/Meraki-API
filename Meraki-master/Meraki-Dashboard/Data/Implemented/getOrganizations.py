# Written by: Tory Davenport
# Description: This script will pull a list of all organizations and organization ID's 
#              availible to the admin account attached the the API key given.

# Import meraki 2/4/2019

from meraki import meraki

# Set Variables
apiKey = "093b24e85df15a3e66f1fc359f4c48493eaa1b73"

# Pull organization information from dashboard (ORGID, NAME) and store in a 
# list called 'organizationKeyDatabase'
organizationDatabase = (meraki.myorgaccess(apiKey))
organizationDatabaseLength = (len(organizationDatabase))

# Tell user how many organizations there are
print("You have", organizationDatabaseLength, "organization(s)")

# Display a list to the user
for item in range(organizationDatabaseLength):
	organizationDatabase[item]


