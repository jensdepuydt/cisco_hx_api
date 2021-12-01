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
$cluster_ip = "172.16.8.10"
$username = "admin"
$password = "password"

$Headers = @{'Content-Type' = 'application/json'}
$aaa_url= "https://$cluster_ip/aaa/v1/auth?grant_type=password"

$Body = @{
    username = "$username"
    password = "$password"
}

$Body = ($Body | ConvertTo-Json)

$r = Invoke-WebRequest -Method 'Post' -Uri $aaa_url -Body $Body -Headers $Headers
$access_token = ConvertFrom-Json $r.Content | Select-Object -expand "access_token"
Write-Host $access_token
