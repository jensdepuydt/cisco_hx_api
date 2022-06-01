#!/usr/bin/python
import json
import requests
import os

# credentials (REPLACE THESE)
cluster_ip = "<cluster_ip>"
username = "<username>"
password = "<password>"

# Authenticate to cluster and get token
# -------------------------------------
headers = {'Content-Type': 'application/json'}
aaa_payload = {
  "username": username,
  "password": password
}
aaa_data = json.dumps(aaa_payload)
aaa_url = "https://"+cluster_ip+"/aaa/v1/auth?grant_type=password"
r = requests.post(aaa_url, aaa_data, headers=headers, verify=False)
access_token = r .json()['access_token']

# Get cluster UUID
# ----------------
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+access_token,
}
url = "https://"+cluster_ip+"/coreapi/v1/clusters"
r = requests.get(url, headers=headers, verify=False)
cluster_uuid = r.json()[0]["uuid"]

# Get cluster about and health
# ----------------------------
url = "https://"+cluster_ip+"/coreapi/v1/clusters/"+cluster_uuid+"/about"
about = requests.get(url, headers=headers, verify=False)
url = "https://"+cluster_ip+"/coreapi/v1/clusters/"+cluster_uuid+"/health"
health = requests.get(url, headers=headers, verify=False)

# Get interesting data from responses
# -----------------------------------
displayVersion = json.loads(about.text)["displayVersion"]
modelNumber = json.loads(about.text)["modelNumber"]
hypervisor = json.loads(about.text)["hypervisor"]
state = json.loads(health.text)["state"]
resiliencyState = json.loads(health.text)["resiliencyDetails"]["resiliencyState"]

# Display fetched info
# --------------------
print ("--- HX Cluster info ---")
print ("- Cluster UUID:", cluster_uuid)
print ("- Cluster Version:", displayVersion)
print ("- Nodes type:", modelNumber)
print ("- Hypervisor:", hypervisor)
print ("- Cluster state:", state, resiliencyState)
