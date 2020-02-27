#!/usr/bin/python3
'''
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
port = 444

serversocket.bind(('',port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("Received connection from ", address)
    message = "Connected to server successfully! " + "\r\n"

    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()
'''

import socket			 

s = socket.socket()		 
print ("Socket successfully created")

 
port = 444				


s.bind(('', port))		 
print ("socket binded to %s" %(port)) 

s.listen(5)	 
print ("socket is listening")			

while True: 

    c, addr = s.accept()	 
    print ('Got connection from', addr )
    message = 'Thank you for connecting'.encode()
    c.send(message) 

    c.close() 
