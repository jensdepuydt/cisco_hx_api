#!/usr/bin/python
import json
import requests

# replace these values to match your environment:
cluster_ip = "172.16.8.10"
username = "admin"
password = "password"

headers = {'content-type': 'application/json'}

aaa_url = "https://"+cluster_ip+"/aaa/v1/auth?grant_type=password"
aaa_payload = {
  "username": username,
  "password": password
}
aaa_data = json.dumps(aaa_payload)

r = requests.post(aaa_url, aaa_data, headers=headers, verify=False)
access_token = r .json()['access_token']
# print (r.status_code)
