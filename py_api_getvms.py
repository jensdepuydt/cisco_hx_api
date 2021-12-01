#!/usr/bin/python
import json
import requests

# replace these values to match your environment:
cluster_ip="172.16.8.10"
access_token = "eyJ...qyg"

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+access_token,
}

url="https://"+cluster_ip+"/rest/virtplatform/vms"
r=requests.get(url,headers=headers,verify=False)
#print (r.status_code)
json_data=json.loads(r.text)
print (json.dumps(json_data, indent=4, sort_keys=True))
