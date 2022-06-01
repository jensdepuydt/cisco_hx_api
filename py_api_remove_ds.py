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

# list existing DS and save them in list
dstodelete = []
url = "https://"+cluster_ip+"/coreapi/v1/clusters/"+cluster_uuid+"/datastores"
r = requests.get(url, headers=headers, verify=False)
json_data = json.loads(r.text)

for ds in json_data:
    if "CLUS" in ds["dsconfig"]["name"]:
        dstodelete.append(ds["uuid"])

print ("Deleting datastores:")
for ds_uuid in dstodelete:
    print ("\n---", ds_uuid)
    url = "https://"+cluster_ip+"/coreapi/v1/clusters/"+cluster_uuid+"/datastores/"+ds_uuid
    print (" - DELETE URL", url)
    r = requests.delete(url, headers=headers, verify=False)
    print (" - HTTP status code:", r.status_code)
