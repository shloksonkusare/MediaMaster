# stop.ps1

# Stop all VLC processes
$vlcProcesses = Get-Process -Name vlc -ErrorAction SilentlyContinue
if ($vlcProcesses) {
    Stop-Process -Name vlc -Force
    Write-Output "All VLC Media Player processes have been stopped."
} else {
    Write-Output "No VLC Media Player processes found."
}

Pause
