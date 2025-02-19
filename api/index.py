# api/index.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = None
        markList = []
         # Parse the URL
        url = urlparse(self.path)
        query_params = parse_qs(url.query)

        with open('q-vercel-python.json', 'r') as file:
            data = json.load(file)

        for key, value in query_params.items():
            for nameValue in value:
                marks = None
                for item in data:
                    if item.get("name") == nameValue:
                        marks = item.get("marks")
                        markList.append(marks)
        
        output = {"marks":markList}
        
        print(data)
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(output).encode('utf-8'))
        return
        
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')  # Allowed methods
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allowed headers
        self.end_headers()

