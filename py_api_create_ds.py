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
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+access_token,
}

# construct URL
url = "https://"+cluster_ip+"/coreapi/v1/clusters/"+cluster_uuid+"/datastores"
print ("- POST URL", url)

# loop and create 5 new datastores
for i in range(1, 6):
    print ("\n------ Create DS", i, "------")

    # create JSON body
    ds_payload = {
      "name": "CLUS DS"+str(i),
      "sizeInBytes": 1073741824,
      "dataBlockSizeInBytes": 8192,
      "usageType": "NFS"
    }
    ds_data = json.dumps(ds_payload)

    # execute POST to URL while passing JSON body
    r = requests.post(url, ds_data, headers=headers, verify=False)
    print ("- HTTP status code:", r.status_code)

    # get new UUID from JSON response
    json_data = json.loads(r.text)
    print ("- New DS UUID:", json_data["uuid"])
