import http.server
import socketserver
import json
import subprocess
import os

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Target the inner launcher folder structure safely
LAUNCHER_DIR = os.path.join(BASE_DIR, "minecraft_system", "launcher_core")

class AdvancedLauncherHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/launch-minecraft':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            data = json.loads(post_data)
            username = data.get('username', 'OfflinePlayer')
            version = data.get('version', '1.20.1')
            
            print(f"\n[SERVER API] Launching -> User: {username}, Ver: {version}")
            
            # Form absolute paths to execution files
            batch_path = os.path.join(LAUNCHER_DIR, "minecraft.bat")
            
            env = os.environ.copy()
            env["MC_USERNAME"] = username
            env["MC_VERSION"] = version
            
            try:
                # cwd=LAUNCHER_DIR isolates file actions to the target subfolder
                subprocess.Popen(batch_path, shell=True, env=env, cwd=LAUNCHER_DIR)
                response_msg = {"status": "success", "message": f"Launcher started for {username}!"}
                status_code = 200
            except Exception as e:
                response_msg = {"status": "error", "message": str(e)}
                status_code = 500
                
            self.send_response(status_code)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_msg).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.path = '/student-playground.html'
        return super().do_GET()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), AdvancedLauncherHandler) as httpd:
        print(f"======================================================")
        print(f"  OFFLINE SERVER ACTIVE AT: http://localhost:{PORT}")
        print(f"  SERVING WEB FILES FROM: {BASE_DIR}")
        print(f"  TARGETING LAUNCHER AT:  {LAUNCHER_DIR}")
        print(f"======================================================")
        httpd.serve_forever()