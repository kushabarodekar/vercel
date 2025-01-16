# api/index.py
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
        # Parse the URL
        url = urlparse(self.path)
        query_params = parse_qs(url.query)
        
        self.wfile.write(json.dumps(getMarksForStudent(query_params)).encode('utf-8'))
        return

    def getMarksForStudent(names):
        with open('../q-vercel-python.json', 'r') as file:
            data = json.load(file)
        return data

