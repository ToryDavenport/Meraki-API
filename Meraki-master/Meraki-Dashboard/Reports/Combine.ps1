$path = "C:\Users\TORYD\OneDrive - FirstLight\FirstLight\Meraki\Meraki-Dashboard\Reports" 
$outfile = "C:\Users\TORYD\OneDrive - FirstLight\FirstLight\Meraki\Meraki-Dashboard\Reports\Save\final.txt"
Get-ChildItem -Path $path -Filter "*.txt" | Get-Content | Add-Content -Path $outfile﻿