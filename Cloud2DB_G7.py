import socket
import time
import psycopg2
import datetime
#create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the ip address of the host i.e gateway and the port
host = "172.20.43.10"
port = 5555
#connecting to the server
sock.connect((host, port))
#connecting to the database
conn = psycopg2.connect(database="G7", user="test", password="root", host="localhost", port="5432")
cursor = conn.cursor()

while True:
	#receiving the data from gateway
	data = sock.recv(1024)
	#converting to the string
	s=data.decode()
	#spliting on "
	temp = s.split('"')
	int_tmp = None
	int_humi = None
	#traversing and storing temperature and humidity
	for i, j in enumerate(temp):
		if j == "temp" and i+1 < len(temp):
			tmp = temp[i+1].strip()[1:-1]
			int_tmp= int(tmp)
		if j == "humi" and i+1 < len(temp):
			humi = temp[i+1].strip()[1:-1]
			int_humi = int(humi)
	#getting todays date
	today = datetime.date.today()
	#getting todays time
	now = time.strftime("%H:%M:%S")
	#fixed node id and device type
	node_id = "fc:69:47:c:2d:43"
	device_id="WiFiMote"
	#query which is to be run so that data is inserted into the database
	query = "INSERT INTO DB_G7 (node_id,device_type,tmp, hmd, dt, tm) VALUES (%s,%s, %s, %s, %s,%s) RETURNING id;"
	data = (node_id,device_id,int_tmp, int_humi,today,now)
	#if there is no data then don't insert into database
	if s!="":
		cursor.execute(query, data)
		print("Recieved")
		conn.commit()
	s="";
	
	
#close the connections
cursor.close()
conn.close()
#close the socket
sock.close()



