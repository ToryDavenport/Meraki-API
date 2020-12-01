$ErrorActionPreference="SilentlyContinue"
Stop-Transcript | out-null
$ErrorActionPreference = "Continue"
Start-Transcript -path C:\Logs\7-15-2019.txt -append
Write-Warning "Logging terminal, type stop-transcript to complete"
python3 Bulk_Import.py