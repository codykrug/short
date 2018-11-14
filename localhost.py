#download embeddable zip file from python.org
#this will create local host (chrome - http://localhost:8000/) will show the python directory listed above
#ctrl-c kills the server

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    
    
