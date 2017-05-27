import socket
import sys
import countminsketch
import json

#read json file
json_data=open("C:\Users\Jose\Desktop\LEIv2\sketch.json")
j = json.load(json_data)

json_data.close()

array = []
i=0

if j['sketchcontroller']['algorithm'] == "count min":
	cm = countminsketch.CountMinSketch(w=272, d=5)
else: print ("wrong algorithm")

writer = open("resultado.json","w")
writer.write("[\n")
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    while True:
        data = sock.recv(36)
        if len(data) == 0:
        	break
        #print >>sys.stderr, 'received "%s"' % data
        parts = data.split()
        cm.update(data);
        array.append(data)

    for j in range(len(array)-1):
    	parts = array[j].split()
        data = [ parts[0][a:a+4] for a in range(0, 8, 4) ]
        data2 = [ data[1][a:a+2] for a in range(0, 4, 2) ]
    	writer.write('{"Ano": ' + "".join(data[0]) +  ', "Mes": "' + "".join(data2[0]) + '", "Dia": "' + "".join(data2[1]) +  '", "Latitude": ' + parts[1] + ', "Longitude": ' + parts[2] + ', "Precipitacao" : ' + parts[3] + ', "Count": ' + str(cm.query(array[j])) + '},\n');
    	#writer.write("{"Data": 20030131, "Latitude": 37.000, "Longitude": -8.800, "Valor" : 0.00, "Count": " + str(cm.query("20030131    37.000   -8.800 0.00")) + "}");
    
    parts = array[len(array)-1].split()
    data = [ parts[0][a:a+4] for a in range(0, 8, 4) ]
    data2 = [ data[a:a+2] for a in range(0, 4, 2) ]
    writer.write('{"Ano": ' + "".join(data[0]) +  ', "Mes": "' + "".join(data2[0]) + '", "Dia": "' + "".join(data2[1]) +  '", "Latitude": ' + parts[1] + ', "Longitude": ' + parts[2] + ', "Precipitacao" : ' + parts[3] + ', "Count": ' + str(cm.query(array[j])) + '},\n');
    writer.write("]")  	

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
    writer.close();