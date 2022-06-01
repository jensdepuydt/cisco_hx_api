# cisco_hx_api

Example scripts to make use of the HX REST API and Intersight API for HX-specific tasks.

## Contents:

### Authentication for Intersight API with Postman:
Environment/variables to set:
- key-id: key ID received when generation API key from intersight (Settings - API Keys - Generate)
- shared-secret: RSA private key from same API key generation (including -----BEGIN RSA PRIVATE KEY-----)

On Postman collection:
Copy postman_intersight_pre-request.js as Pre-request Script to sign HTTP requests for authentication to Intersight with the values entered in the above variables.
This script will also replace characters in the URL (UriEncode), including single quotes (which are not properly handled by Intersight).

For each request, add the following headers:
- Accept: application/json
- Authorization: Signature {{httpsig}}
- Digest: {{computed-digest}}
- Date: {{current-date}}

### Python scripts for HX REST API:
Sample scripts for authentication and basic actions on HX REST API.
py_api_auth.py can be combine with the rest of the scripts to re-authenticate instead of using an access_token (Bearer).

- py_api_auth.py: Authentication and getting access_token in a variable
- py_api_get_cluster_uuid.py: Fetch cluster UUID in a variable
- py_api_get ds.py: Get a list of current datastores on the HX cluster
- py_api_create_ds.py: Create 5 datastores on the HX cluser
- py_api_remove_ds.py: Remove the 5 created datastores from the HX cluster
- py_api_getvms.py: Get a list of all VMs on the HX cluster
- py_api_cluster_info.py: Combined script (auth/cluster_uuid) to fetch generic cluster info and state

### Powershell scripts for HX REST API:
Sample scripts for authentication and basic actions on HX REST API.
ps_api_auth.ps1 can be combine with the rest of the scripts to re-authenticate instead of using an access_token (Bearer).

- ps_api_auth.ps1: Authentication and getting access_token in a variable
- ps_api_example.ps1: Combined authentication and get request for all VMs
- ps_api_getvms.ps1: Get a list of all VMs on the HX cluster

