
$startTime = Get-Date

./a.exe

$endTime = Get-Date

$executionTime = $endTime - $startTime

Write-Host "Script took $($executionTime.TotalSeconds) seconds to execute."
