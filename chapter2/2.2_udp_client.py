#!/usr/bin/python

import socket

target_host = raw_input("Enter the host: ")
target_port = int(raw_input("Enter the port number: "))

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto('AAABBBCCC',(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)

print data
