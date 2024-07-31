from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import subprocess
import socket

class RequestHandler_httpd(BaseHTTPRequestHandler):
    shell_process = None

    def do_GET(self):
        # Parse the query parameters
        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        action = query_components.get('action', None)
        path = query_components.get('path', None)

        if action:
            if action[0] == 'run' and path:
                self.run(path[0])
                response = "<html><body><h1>Running</h1></body></html>"
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(response))
                self.end_headers()
                self.wfile.write(bytes(response, "utf-8"))
            elif action[0] == 'stop':
                self.stop(force=True)
                response = "<html><body><h1>Stopped</h1></body></html>"
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(response))
                self.end_headers()
                self.wfile.write(bytes(response, "utf-8"))
            else:
                self.send_error(400, "Invalid action or missing parameters")
        else:
            self.send_error(400, "Invalid or missing action parameter")

    def run(self, path):
        # Stop any currently running process forcefully
        self.stop(force=True)
        
        if path.endswith('.ps1'):
            # Command to run the PowerShell script
            command = f"powershell.exe -ExecutionPolicy Bypass -File \"{path}\""
        else:
            # Command to run the PowerShell script to play a video file with VLC
            command = f"powershell.exe -ExecutionPolicy Bypass -File D:\\Shlok\\VUElectronics\\play_video.ps1 -videoPath \"{path}\""
        
        self.shell_process = subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        print(f"Started process with PID: {self.shell_process.pid}")

    def stop(self, force=True):
        # Stop the currently running shell process
        if self.shell_process:
            try:
                self.shell_process.terminate()
                self.shell_process.wait(timeout=5)
                print(f"Terminated process with PID: {self.shell_process.pid}")
            except subprocess.TimeoutExpired:
                if force:
                    self.shell_process.kill()
                    print(f"Force killed process with PID: {self.shell_process.pid}")
            self.shell_process = None

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Connect to an external server to get the local IP address
        s.connect(("8.8.8.8", 80))
        
        # Get the IP address
        ip_address = s.getsockname()[0]
        
        # Close the socket
        s.close()
        
        return ip_address
    except Exception as e:
        return str(e)

def run():
    ip_address = get_ip_address()
    if ip_address:
        server_address_httpd = (ip_address, 8080)
        httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
        print(f'Starting Server on {ip_address}...')
        httpd.serve_forever()
    else:
        print("Failed to get IP address")

if __name__ == '__main__':
    run()
