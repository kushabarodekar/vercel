# api/index.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = None
         # Parse the URL
        url = urlparse(self.path)
        query_params = parse_qs(url.query)

        with open('q-vercel-python.json', 'r') as file:
            data = json.load(file)
        print(data)
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return

