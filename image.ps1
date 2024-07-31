param (
    [string]$imagePath
)

# Check if VLC is installed
$vlcPath = "C:\Program Files\VideoLAN\VLC\vlc.exe"
if (-not (Test-Path $vlcPath)) {
    Write-Error "VLC Media Player is not installed in the default path."
    exit 1
}

# Construct the VLC command to display the image in fullscreen and loop
$vlcCommand = """$vlcPath"" ""$imagePath"" --fullscreen --image-duration=999999 --loop"

# Start VLC with the constructed command
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoLogo", "-NoProfile", "-Command", $vlcCommand
