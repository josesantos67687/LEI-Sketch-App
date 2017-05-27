import socket
import sys
import glob
import time
import json

#read json file
json_data=open("C:\Users\Jose\Desktop\LEIv2\wraper.json")
j = json.load(json_data)

json_data.close()

start_time = time.time()

pathfiles = glob.glob("C:\Users\Jose\Desktop\LEIv2\*" + j['wrapercontroller']['type'])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        print >>sys.stderr, 'sending data to the client'
        for fpath in pathfiles:
                        file = open(fpath,"r");
                        for line in file:
                                time.sleep(j['wrapercontroller']['timelaps'])
                                c = line.rstrip("\n")
                                parts = c.split()
                                if len(parts)==1:
                                        data = c
                                else :
                                        message = data + " " + c
                                        connection.send(message)
            
    finally:
        # Clean up the connection
        connection.close()
