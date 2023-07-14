import socket
import time
import random
# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a public host and port
host = "172.20.43.10"  # Get the hostname of the server
port = 5555               # Reserve a port for your service.
sock.bind((host, port))     # Bind to the socket to the hostname and port

# Listen for incoming connections
sock.listen(5)              # Allow up to 5 pending connections

#print("Server is listening for incoming connections...")
client, address = sock.accept()
print(f"Got a connection from {address}")
cnt=0
fi=open("recordData_G7", "r")
while True:
	#if count is less than 5 then we read the data and send it
	if cnt<5:
		#fi=open("log.txt", "r")
		message = fi.readline()
		print(message)
		client.send(message.encode())
		cnt=cnt+1;
		time.sleep(5)
	#if cnt==5 then it clears the file and re-updates it	
	if cnt==5:
		cnt=0;
		fil=open("recordData_G7", "r+")
		cont=fil.read();
		lines=cont.split('\n')
		fil.truncate(0)
		fil.close()
		fil=open("recordData_G7", "a")
		temp=0
		for l in lines:
			if temp<5:
				temp=temp+1
				continue
				
			fil.write(l)
			fil.write('\n')
		fil.close()
		time.sleep(5)
		
client.close()
fi.close()
