#!/usr/bin/python

import socket

target_host = raw_input("Enter the host: ")
target_port = int(raw_input("Enter the port number: "))

# this information will be sent to the server
host = raw_input("Enter the header --> Host: ")

# create a socket object --> socket.socket(family, type)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to the target
client.connect((target_host,target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: "+host+"\r\n\r\n")

# receive some data client.recv(buffersize)
response = client.recv(4096)

print response
