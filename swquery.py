# This script connects to Solarwinds API using orionsdk and queries for devices matching category *AN (WAN, MAN or LAN) and
# returns the results alphabetically by SysName

import getpass
import requests
import ast
import json
from orionsdk import SwisClient

npm_server = 'your.solarwinds.server' # add your solarwinds server
username = 'netansible'
password = getpass.getpass("Enter password: ")
verify = False
if not verify:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



swis = SwisClient(npm_server, username, password)
# Your SW database may have other values for Category
print ("Query Test: ")
results = swis.query("SELECT SysName FROM Orion.Nodes WHERE Orion.Nodes.Category LIKE '%AN%' ORDER BY SysName")

uri = results['results']

# ast.literal_eval removes 'u from list output
uri  = ast.literal_eval(json.dumps(uri))

for i in uri:
    print i['SysName']
