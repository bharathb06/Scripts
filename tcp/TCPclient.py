#!/usr/bin/python3

'''
import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname
port = 444

clientsocket.connect(('127.0.0.1',port))

message = clientsocket.recv(1024) #max data to be allowed/recvd on the port

clientsocket.close()

print(message.decode("ascii"))

'''
import socket			 

s = socket.socket()		 

port = 444			

s.connect(('127.0.0.1', port)) 

print (s.recv(1024)) 
s.close()	 
