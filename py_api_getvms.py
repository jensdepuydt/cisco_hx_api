#!/usr/bin/python
import json
import requests

# replace these values to match your environment:
cluster_ip = "<cluster_ip>" # REPLACE THIS
if 'HX_ACCESS_TOKEN' in os.environ:
    access_token = os.environ['HX_ACCESS_TOKEN']
else:
    access_token = input("Please provide the access_token for HX:")

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+access_token,
}

url="https://"+cluster_ip+"/rest/virtplatform/vms"
r=requests.get(url,headers=headers,verify=False)
#print (r.status_code)
json_data=json.loads(r.text)
print (json.dumps(json_data, indent=4, sort_keys=True))
