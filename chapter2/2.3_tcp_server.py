#!/usr/bin/python

import socket
import threading

bind_ip = raw_input("Enter the binding IP Address: ")
bind_port = int(raw_input("Enter the port to bind to: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on "+str(bind_ip)+":"+str(bind_port)

# client handling thread
def handle_client(client_socket):

    # print out whatever the client sends
    request = client_socket.recv(1024)

    print "[*] Received :\n"+str(request)

    #send back a packet
    client_socket.send("ACK!")

    client_socket.close()

while True:
    client,addr = server.accept()

    print "[*] Accepted connection from "+str(addr[0])+":"+str(addr[1])

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
