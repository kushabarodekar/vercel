# api/index.py
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
         # Parse the URL
        url = urlparse(self.path)
        query_params = parse_qs(url.query)
        
        # Log query parameters
        #print(f"Query parameters: {query_params}")
        

        #print(getMarks(query_params))
        # Respond to the client
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
        # Parse the URL
        url = urlparse(self.path)
        query_params = parse_qs(url.query)

        print(getMarks(query_params))
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return

    def getMarks(names):
        print(names)
        #with open('q-vercel-python.json', 'r') as file:
        #    data = json.load(file)
        #print(data)
        return names

