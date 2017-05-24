import socket

target_host = raw_input("Enter the host: ")
target_port = raw_input("Enter the port number: ")

# create a socket object
client = socket.socket