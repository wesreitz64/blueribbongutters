from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import json
import os
from datetime import datetime

# Directory to save logs
LOG_DIR = "visitor_logs"
os.makedirs(LOG_DIR, exist_ok=True)
VISITORS_FILE = os.path.join(LOG_DIR, "visitors.json")

# Initialize file if it doesn't exist
if not os.path.exists(VISITORS_FILE):
    with open(VISITORS_FILE, 'w') as f:
        json.dump([], f)

class TrackerHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.0" # Prevents Keep-Alive hanging

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        # Serve the visitors.json file at /api/visitors
        if self.path == '/api/visitors':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            with open(VISITORS_FILE, 'r') as f:
                self.wfile.write(f.read().encode())
        else:
            return super().do_GET()

    def do_POST(self):
        if self.path == '/track':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                
                # Load existing data
                with open(VISITORS_FILE, 'r') as f:
                    visitors = json.load(f)
                
                # Append new data
                data['_server_received_at'] = datetime.now().isoformat()
                visitors.insert(0, data) # Put newest first
                
                # Keep only last 100 visitors
                visitors = visitors[:100]
                
                # Save back to file
                with open(VISITORS_FILE, 'w') as f:
                    json.dump(visitors, f, indent=2)
                
                print(f"✅ Received visitor data from IP: {self.client_address[0]}")
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"status": "success"}')
                
            except Exception as e:
                print(f"Error processing tracker data: {e}")
                self.send_response(500)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    port = 8080
    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, TrackerHandler)
    print(f"🚀 Tracking Server running on port {port}")
    print(f"   Dashboard: http://localhost:{port}/admin-visitors.html")
    print(f"   Track endpoint: http://localhost:{port}/track")
    httpd.serve_forever()
