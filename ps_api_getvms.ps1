# workaround when using a self-signed certificate on your HX cluster
add-type @"
    using System.Net;
    using System.Security.Cryptography.X509Certificates;
    public class TrustAllCertsPolicy : ICertificatePolicy {
        public bool CheckValidationResult(
            ServicePoint srvPoint, X509Certificate certificate,
            WebRequest request, int certificateProblem) {
            return true;
        }
    }
"@
[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls -bor [Net.SecurityProtocolType]::Tls11 -bor [Net.SecurityProtocolType]::Tls12

# replace these values to match your environment:
$cluster_ip="172.16.8.10"
$access_token = "eyJ...qyg"

$Headers = @{
	'Content-Type' = 'application/json'
    'authorization' = "Bearer $access_token"
    }

$url= "https://$cluster_ip/rest/virtplatform/vms"

Invoke-RestMethod -Method 'Get' -Uri $url -Headers $Headers
