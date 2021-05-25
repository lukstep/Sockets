import socket
import argparse

HOST = 'localhost'
parser = argparse.ArgumentParser()
parser.add_argument('--port', dest='port', type=int, help="Process port")
args = parser.parse_args()

print("Client port:{0}".format(args.port))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created")
    s.connect((HOST, args.port))
    while True:
        a = input()
        s.send(a.encode('ascii'))
        data = s.recv(1025)
        print(data.decode('ascii'))