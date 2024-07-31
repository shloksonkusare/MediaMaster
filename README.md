# MediaMaster Control

## Overview
MediaMaster Control is a project that allows users to manage media playback, including images and videos, through a web server. It utilizes Python and PowerShell scripts to control the playback of media files on a local machine using VLC Media Player.

## Features
- **Run Videos**: Play the videos on the VLC Media Player with the options of fullscreen and looping.
- **Display Images**: Show images in fullscreen mode in VLC Media Player.
- **Stop Media**: Stop all the media running playback and all associated processes.
- **Stop Python processes**: Stop all the python processes with a single command.
- **System Shutdown**: Initiate system shutdown through the web interface.

## Technologies Used
1. **Python**: For the web server and handling the HTTP requests.
2. **PowerShell**: For executing the media playback commands and controlling the system.
3. **VLC Media Player**: For playing video or image files.
4. **HTTP Server**: to accept requests and manage media playback.

## Installation
### Prerequisites
- **Python**: Ensure Python is installed in your machine.
- **VLC Media Player**.
- **PowerShell**.

## Set up Scripts:
- **start.bat**: Initializes the python program, this file is helpful when we have to execute the python program during certain events like Power ON, etc.
- **run_hidden.vbs**: This file ensures that the start.bat file should be executed in the background, without opening the terminal. 
- **play_video.ps1**: Script to play videos in fullscreen and in looping manner.
- **image.ps1**: Script to display images in fullscreen and in looping manner.
- **stop.ps1**: Script to stop the execution of current video or image on the system.
- **abort.ps1**: Script to stop the execution of the python programs in the system.
- **shutdown.ps1**: Script to shut down the system forcefully.

## Usage

### Starting the Server
To start the server, execute the python file in the command prompt.
```python server.py```
The server will start and listen for requests on the local IP address at port _8080_.

### Sending Requests
1. Run a Video:
```http://<server_ip>:8080/?action=run&path=C:\path\to\video.mp4```
2. Display an Image:
```http://<server_ip>:8080/?action=run&path=C:\path\to\image.jpg```
3. Execute a PowerShell Script:
```http://<server_ip>:8080/?action=run&path=C:\path\to\script.ps1```

## Troubleshooting
**Execution Policy:** If you encounter execution policy errors when running PowerShell scripts, you can bypass the policy temporarily using:
```Set-ExecutionPolicy Bypass```