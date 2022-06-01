#!/usr/bin/python
import json
import requests
import os

# get access token from env var
cluster_ip = "<cluster_ip>" # REPLACE THIS
if 'HX_ACCESS_TOKEN' in os.environ:
    access_token = os.environ['HX_ACCESS_TOKEN']
else:
    access_token = input("Please provide the access_token for HX:")

# set headers
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+access_token,
}

# construct URL
url = "https://"+cluster_ip+"/coreapi/v1/clusters"
print ("- GET URL", url)

# execute GET to URL
r = requests.get(url, headers=headers, verify=False)
print ("- HTTP status code:", r.status_code)

# show raw response in JSON
print ("- Raw JSON response: ")
json_data = json.loads(r.text)
print (json.dumps(json_data, indent=4, sort_keys=True))

# get cluster UUID
cluster_uuid = r.json()[0]["uuid"]
print ("\n- Extracted cluster_uuid:", cluster_uuid)
print ("\n- export HX_CLUSTER_UUID="+cluster_uuid)
