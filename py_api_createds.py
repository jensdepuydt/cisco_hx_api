#!/usr/bin/python
import json
import requests

# replace these values to match your environment:
cluster_ip = "172.16.8.10"
access_token = "eyJ...qyg"
cluster_uuid = "9004183636114227531:5445300663653806560"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+access_token,
}

url = "https://"+cluster_ip+"/coreapi/v1/clusters/"+cluster_uuid+"/datastores"
ds_payload = {
  "name": "cleur_ds",
  "sizeInBytes": 1073741824,
  "dataBlockSizeInBytes": 8192,
  "usageType": "NFS"
}
ds_data = json.dumps(ds_payload)

r = requests.post(url, ds_data, headers=headers, verify=False)
# print (r.status_code)
json_data = json.loads(r.text)
print (json.dumps(json_data, indent=4))
