# play_video.ps1 content
param (
    [string]$videoPath
)

# Kill any existing VLC processes
$vlcProcesses = Get-Process -Name vlc -ErrorAction SilentlyContinue
if ($vlcProcesses) {
    Stop-Process -Name vlc -Force
}

# Path to VLC Media Player executable
$vlcPath = "C:\Program Files\VideoLAN\VLC\vlc.exe"

# Command to play the video in fullscreen and loop
$command = "& `"$vlcPath`" --fullscreen --loop `"$videoPath`""

# Start VLC with the command
Invoke-Expression $command
