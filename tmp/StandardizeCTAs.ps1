
$res = "C:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build\residential-security-singapore.html"
$com = "C:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build\commercial-security-singapore.html"

# Fix WhatsApp
(Get-Content $res) -replace 'WhatsApp Us', 'WhatsApp an Engineer' | Set-Content $res
(Get-Content $com) -replace 'WhatsApp Us', 'WhatsApp an Engineer' | Set-Content $com

# Fix Button Group Spacing
(Get-Content $res) -replace '<div class="btn-group mt-32">', '<div class="btn-group mt-48">' | Set-Content $res
(Get-Content $com) -replace '<div class="btn-group mt-32">', '<div class="btn-group mt-48">' | Set-Content $com
