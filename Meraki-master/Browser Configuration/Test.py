from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Launch chrome's web driver 
driver = webdriver.Chrome()
# Bring up URL
organizations = ['CAPCO - S Main Church',
					'CCC Housing Company, LLC',
					'CFCU Community Credit Union',
					'Canandaigua Chamber',
					'Canandaigua Family YMCA',
					'Canfield & Tack',
					'CenterBridge Planning Group',
					'City of Buffalo',
					'City of Buffalo (Dillon)',
					'City of Ithaca',
					'Commerce Chenango',
					'Cornell Heights Apts.',
					'Cornell University Press - Sage House',
					'Crouse Medical Practice',
					'DHL Drawback Services',
					'Danforth',
					'Dermatology Associates of Rochester',
					'Dover High School',
					'Eaton Center',
					'Entre Computer Services',
					'FLTG at Pinnacle Athletic Campus',
					'Fenton Free Library',
					'Finger Lakes Ambulance Service',
					'Finger Lakes Racetrack',
					'Finger Lakes Technologies Group',
					'Finger Lakes Technologies Group Inc.',
					'Finger Lakes Welcome Center',
					'FirstLight (OFC Returns)',
					'G.W. Lisk, Inc.',
					'GiveGab',
					'Ithaca Tompkins Regional Airport',
					'LCSD Wireless',
					'LaBella Associates',
					'Lago Casino and Resort',
					'Lago Casino and Resort-2',
					'Lake St Presbyterian Church',
					'Lefrois Builders',
					'Letchworth CSD',
					'Lifetime Assistance, Inc',
					'Lifetime Assistance, Inc',
					"Lynne Parks '68 SUNY Cortland Alumni House",
					'MOJO Sells',
					'Maguire Honda (formerly Honda Of Ithaca)',
					'Moll Properties',
					'Motor Components',
					'NITTEC',
					'Nathan Littauer Hospital',
					'Nucor Steel',
					"O'Brien's Barber Shop",
					'ORGANIZATION_TEMPLATE',
					'Opportunities for Broome',
					'Opportunities for Chenango',
					'Peters Supply',
					'Pi Kappa Phi',
					'REV: Ithaca Startup Works',
					'RYCO - Powder Mill Land Co',
					'RYCO Management',
					'Railside Market & Cafe',
					'Relph Benefits',
					'Rochester Academy Charter School',
					'Rochester Drug Cooperative, Inc.',
					'Rohm Services',
					'SHBC HCS Customers',
					'SWBR Architects',
					'Seager Marine',
					'Seneca Cayuga ARC',
					'Sigma Nu',
					'Skaneateles Central Schools',
					'Southern Tier High Technology Incubator',
					'TC3 Coltivare Arts Center',
					'Tompkins County',
					'Tradition Chevy',
					'Travis-Hyde/516 University/Ravenwood',
					'URSA Space Systems Inc',
					'Utica First Insurance',
					'VanBortel Corvette',
					'Velocitii',
					'Village of Sherburne',
					'Waffle Frolic',
					'Webster Property Management, LLC (Elmwood)',
					'Wells College',
					'West Shore Apartments',
					'Yates House',
					'eCornell']
try:
	for org in organizations:
		driver.get('https://account.meraki.com/secure/login/dashboard_login')
		
		username = driver.find_element_by_name("email")
		username.send_keys("tdavenport@firstlight.net")
		password = driver.find_element_by_name("password") 
		password.send_keys("01E!&3zRU$")
		
		driver.find_element_by_name("commit").click()
		
		driver.find_element_by_partial_link_text(f'{org}').click()
		driver.find_element_by_partial_link_text('Network-wide').click()
		driver.find_element_by_partial_link_text('Alerts').click()
		sleep(2)
		driver.find_element_by_class_name('SaveChanges').click()
		sleep(2)
		driver.find_element_by_class_name('TableEditor__addButton').click()
		sleep(2)
		driver.find_element_by_name("http-servers[0][name]").send_keys("Zapier")
		driver.find_element_by_name("http-servers[0][url]").send_keys("https://hooks.zapier.com/hooks/catch/5235423/oyiin5w/")
		sleep(3)
		driver.find_element_by_class_name('btn-primary').click()
		sleep(1)
except Exception as e:
	print(e)
	pass
		