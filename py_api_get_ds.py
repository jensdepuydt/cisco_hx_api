#!/usr/bin/python
import json
import requests
import os

# get access token and cluster uuid from env var
cluster_ip = "<cluster_ip>" # REPLACE THIS
if 'HX_ACCESS_TOKEN' in os.environ:
    access_token = os.environ['HX_ACCESS_TOKEN']
else:
    access_token = input("Please provide the access_token for HX:")
if 'HX_CLUSTER_UUID' in os.environ:
    cluster_uuid = os.environ['HX_CLUSTER_UUID']
else:
    cluster_uuid = input("Please provide the cluster_uuid for HX:")

# set headers
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+access_token,
}

# construct URL
url = "https://"+cluster_ip+"/coreapi/v1/clusters/"+cluster_uuid+"/datastores"
print ("- GET URL", url)

# execute GET to URL
r = requests.get(url, headers=headers, verify=False)
print ("- HTTP status code:", r.status_code)

# show raw response in JSON
print ("- Raw JSON response: ")
json_data = json.loads(r.text)
print (json.dumps(json_data, indent=4, sort_keys=True))

# extract useful info and format output
print ("\n- Formatted response: ")
for ds in json_data:
    print ("\n---", ds["dsconfig"]["name"], "-", ds["uuid"])
    size = round(float(ds["totalCapacityInBytes"])/1073741824, 2)
    free = round(float(ds["freeCapacityInBytes"])/1073741824, 2)
    print ("    Free:", str(free), "/", str(size), "GB")
    print ("    Mounted:", ds["mountSummary"])
