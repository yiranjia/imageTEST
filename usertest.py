#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from art import apply_mask
import http.client



# HTTPRequestHandler class
class userHandler(BaseHTTPRequestHandler):
    # GET
     def do_GET(self):
        # Send response status code
        self.send_response(200)
        print()
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        style = self.path[8:]
        print (style)
        #do_something(style, 'some hard code path')
        apply_mask(style,"https://s3.amazonaws.com/cyberbrush/ryan.jpg")
        # image
        # Send message back to client
        message = style
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return




def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, userHandler)
    print('running server...')
    httpd.serve_forever()


run()
