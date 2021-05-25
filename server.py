#!/usr/bin/env python3
import socket
import argparse

HOST = '0.0.0.0'  

parser = argparse.ArgumentParser()
parser.add_argument('--port', dest='port', type=int, help="Process port")
args = parser.parse_args()

print("Server port:{0}".format(args.port))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, args.port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data.decode('ascii'))
            if not data:
                break
            conn.sendall(data)