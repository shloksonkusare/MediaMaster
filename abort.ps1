# Get all running Python processes and stop them
Get-Process -Name python -ErrorAction SilentlyContinue | Stop-Process -Force
