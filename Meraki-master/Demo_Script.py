# To import a module, subpackage or object (class or function)
from meraki import meraki as dashboard
import json

# Variable assignment 
api_key = "REDACTED"

# Return organizations and store in a data structure
organization_list = dashboard.myorgaccess(api_key)
# print(type(organization_list))
# Count organizations returned
organization_length = len(organization_list)

# Write a JSON parser function
def print_orgs():
	for item in range(organization_length):
		# Access each individual item in the list and print it out
		json_data = json.dumps(organization_list[item], indent = 4)
		print(json_data)

# Add organization 
dashboard.addorg(api_key, "TEST ORG, LLC")

# Function call
print_orgs()
