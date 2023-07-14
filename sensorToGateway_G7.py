import socket
import sys
import time
import json
import _thread

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port on the server given by the caller
#serv_ip = raw_input("Enter the Server IP:")
com_port = 5556

server_address = ('', int(com_port))
# print >>sys.stderr, 'connecting to %s port %s' % server_address

print('connecting to %s port %s' % server_address, file=sys.stderr)
#socket is listening to particular address and port
sock.bind(server_address)
sock.listen(5)
try:
    while True:
    	#accepting the connection
        s, addr = sock.accept()
        #receiving the data from sensor
        data = s.recv(100)
        print(data)
        #converting data to string
        tempData=data.decode()
        #splitting the data on "
        tempD=tempData.split('"')
        for i in tempD:
        	print(i)
        	#if node id is our id open the file and write
        	if str(i)=="fc:69:47:c:2d:43":
        		f=open("recordData_G7","a")
        		f.write(tempData)
        		f.write('\n')
        		f.close()
        #for sending 10 entries per minute
        time.sleep(6)
        #closing the connection
        s.close()
finally:
    sock.close()
