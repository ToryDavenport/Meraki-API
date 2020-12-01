from meraki import meraki

# Instantiate Variables
apiKey = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
organizationID = '578149602163689012'
suppressPrint = True
organizationIdNumberList = []
organizationDatabase = (meraki.myorgaccess(apiKey, suppressPrint))
organizationDatabaseLength = (len(organizationDatabase))

def generateOrgIDList( apiKey, organizationID, suppressPrint, organizationDatabase, organizationDatabaseLength ):
	# Iterate throught he list and extract the data. Output clean data
	for i in range(organizationDatabaseLength):
		# Convert the dictionary values to a list
		organization_list = list(organizationDatabase[i].values())
		# Select the Organization ID
		organization_ID = str(organization_list[0])
		organizationIdNumberList.append(organization_ID)
		print(organizationIdNumberList[i])

generateOrgIDList( apiKey, organizationID, suppressPrint, organizationDatabase, organizationDatabaseLength)



