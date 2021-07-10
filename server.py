#!/usr/bin/env python3
import socket
import argparse
import socketserver

HOST = '0.0.0.0'  

parser = argparse.ArgumentParser()
parser.add_argument('--port', dest='port', type=int, help="Process port")
args = parser.parse_args()

print("Server port:{0}".format(args.port))

class TCPHanndler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        self.data = self.request.recv(1024).strip()
        print("{} wrote".format(self.client_address[0]))
        print(self.data)
        # self.request.sendall(self.data.upper())

with socketserver.TCPServer((HOST, args.port), TCPHanndler) as server:
    server.serve_forever()
