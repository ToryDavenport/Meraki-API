# Written by Tory Davenport
# Description: Add admins to an organization (Allow single mode and bulk edit)
# Last Updated: 2/4/2019
from meraki import meraki



# Set apiKey and organization
apiKey = ''
#organizationID = '578149602163689012'
suppressPrint = True
organizationIdNumberList = []
organizationNamesList = []
organizationDatabase = (meraki.myorgaccess(apiKey, suppressPrint))
organizationDatabaseLength = (len(organizationDatabase))


# To add multiple admins to one organization
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
	

def generateOrgIDList( apiKey, organizationDatabase, organizationDatabaseLength ):
	# Iterate throught he list and extract the data. Output clean data
	for item in range(organizationDatabaseLength):
		# Convert the dictionary values to a list
		organization_list = list(organizationDatabase[item].values())
		# Select the Organization ID
		organization_ID = str(organization_list[0])
		organizationName = str(organization_list[1])
		organizationNamesList.append(organizationName)
		organizationIdNumberList.append(organization_ID)
		#print(organizationIdNumberList[item])
	return

def getAdminAll ( apiKey, organizationDatabase, organizationDatabaseLength ):
	for item in range(organizationDatabaseLength):
		# Enter organization ID to begin operation
		organizationID = organizationIdNumberList[item]
		organizationName = organizationNamesList[item]
		#print(organizationID)
		print()
		# New admin variables
		adminReport( apiKey, organizationID, organizationName, suppressPrint )
	clear()
# Write function that formats admins list and call within getAdminAll . . .
def adminReport( apiKey, organizationID, organizationName, suppressPrint ):
	#clear()
	# GET list of admins
	adminsList = meraki.getorgadmins(apiKey,organizationID,suppressPrint)
	# Find the length of the list
	adminsListLength = len(adminsList)
	print("Here is the list of admins for organization name:","'"+organizationName+"',", "ID #:",organizationID)
		# Iterate throught he list and extract the data. Output clean data
	for item in range(adminsListLength):
		# Convert the dictionary values to a list
		admin_list = list(adminsList[item].values())
		# Select the Admin Name
		admin_name = str(admin_list[0])
		# Select the Admin's Email
		admin_email = str(admin_list[1])
		# Select the Admin ID to print
		admin_ID = str(admin_list[2])
		# Select the Two-Factor Auth.
		admin_TwoFactor = str(admin_list[5])
		# Select Last Active
		admin_LastActive = str(admin_list[6])
		# Select account status
		admin_AccountStatus = str(admin_list[7])
		# Select Organization Access Level
		admin_OrganizationLevel = str(admin_list[8])
		# Print Values
		print("\nName: " + admin_name, "\nEmail: " + admin_email, "\nAdmin ID #: " + admin_ID, "\nTwo-Factor Authentication: " + admin_TwoFactor, "\nLast Active: " + admin_LastActive, "\nAccount status: " + admin_AccountStatus, "\nOrganization Access Level: " + admin_OrganizationLevel)
	#input("\nPress any key to continue. . .")
	#clear()
	return

generateOrgIDList( apiKey, organizationDatabase, organizationDatabaseLength )
bulk_add_multiple_organizations( api_key, organization_database_length )
#getAdminAll ( apiKey, organizationDatabase, organizationDatabaseLength )