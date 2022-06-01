#!/usr/bin/python
import json
import requests
import os

# credentials (REPLACE THESE)
cluster_ip = "<cluster_ip>"
username = "<username>"
password = "<password>"

# set headers
headers = {'Content-Type': 'application/json'}

# create JSON body
aaa_payload = {
  "username": username,
  "password": password
}
aaa_data = json.dumps(aaa_payload)

# construct URL
aaa_url = "https://"+cluster_ip+"/aaa/v1/auth?grant_type=password"
print ("- POST URL", aaa_url)

# execute POST to URL while passing JSON body
r = requests.post(aaa_url, aaa_data, headers=headers, verify=False)
print ("- HTTP status code:", r.status_code)

# show raw response in JSON
print ("- Raw JSON response: ")
json_data = json.loads(r.text)
print (json.dumps(json_data, indent=4, sort_keys=True))

# get access token
access_token = r .json()['access_token']
print ("\n- Extracted access_token:", access_token)
print ("\n- export HX_ACCESS_TOKEN="+access_token)
