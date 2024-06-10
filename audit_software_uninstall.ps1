# Define the Sysmon log name
$sysmonLogName = "Microsoft-Windows-Sysmon/Operational"
$messageFilter = "*prtg*"

# Define the event IDs to look for (process creation and file creation)
$eventIds = 1, 11, 13

# Get the current time and calculate the start time for 24 hours ago
$endTime = Get-Date
$startTime = $endTime.AddHours(-1)
#search last hour
#$startTime = $endTime.AddDays(-1)
#search last 24 hours
$outputResult = "audit.txt"

# Query the Sysmon logs for events related to uninstallation of PRTG
Get-WinEvent -FilterHashtable @{LogName=$sysmonLogName; Id=$eventIds; StartTime=$startTime; EndTime=$endTime} | 
    Where-Object { $_.Message -like $messageFilter -and $_.Message -match "(?i)uninstall|remove|delete" } |
    Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message|Out-File $outputResult
