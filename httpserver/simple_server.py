from http.server import HTTPServer, SimpleHTTPRequestHandler

def trans(arg):
  return arg.upper()

class Handler(SimpleHTTPRequestHandler):
  def do_GET(self):
    body = trans(self.path)
    body = bytes(body, 'utf-8') 
    self.send_response(200)
    self.send_header('Content-type', 'text/html;charset=utf-8')
    self.send_header('Content-length', len(body))
    self.end_headers()
    self.wfile.write(body)
    
host = 'localhost'
port = 8000
httpd = HTTPServer((host, port), Handler)
print('serving@%d 🎾' % port)
httpd.serve_forever()

"Client.py would be like this..."
"""
import urllib.request
with urllib.request.urlopen('http://localhost:8000') as res:
  html = res.read().decode('utf-8')
  print(html)
"""
