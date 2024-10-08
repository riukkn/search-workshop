from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from search import do_search
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self): 
    parsed_path = urlparse(self.path)
    query_params = parse_qs(parsed_path.query)
    # Query params
    field = query_params.get('field', ['title'])[0]
    query = query_params.get('query', [''])[0]
    limit = query_params.get('limit', [10])[0]
    
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    results = do_search(field, query, int(limit))

    return self.wfile.write(json.dumps({
      'field': field,
      'query': query,
      'limit': limit,
      'results': results
    }).encode('utf-8'))

server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Serving on port 8000...")
httpd.serve_forever()