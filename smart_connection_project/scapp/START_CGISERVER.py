import SimpleHTTPServer
import SocketServer
import CGIHTTPServer

from CGIHTTPServer import CGIHTTPRequestHandler
from BaseHTTPServer import HTTPServer


server_address=('',8000)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

httpd.serve_forever()