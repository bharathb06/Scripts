#1/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = input("Enter the ip: ")                         #"137.74.187.102"
port = int(input("Enter port: "))


def portScan(port):
    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")

portScan(port)    