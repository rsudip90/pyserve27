import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import webbrowser as wb
import threading

def server_files():
    wb.open("http://127.0.0.1:8008")


HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

port = 8008
server_address = ('0.0.0.0', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()

t = threading.Thread(target=server_files)
t.start()

print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()