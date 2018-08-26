import socket 
import sys
import select
import threading

HOST, PORT = "localhost", 9999


#create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	# connect to server and send data
	sock.connect((HOST, PORT))
	sock.setblocking(0)

	send_queue = []

	# Recieve data from the server and assign user name
	sent = ""
	ready = select.select([sock],[],[],1)
	if ready[0]:
		recieved = str(sock.recv(1024), "utf-8")
		print("recv: {}".format(recieved))
	username = recieved[11:]

	# Join message client side
	print(username + " new user")
	
	# spin up chat 
	while sent != "exit()":
	
		ready = select.select([sock], [], [], 1)
		if ready[0]:
			recieved = str(sock.recv(1024), "utf-8")
			print(recieved)

		sent = input(": ")
		send_queue.append(sent)
		
		
		#while send_queue:
		#sent = send_queue.pop(0)
		sock.send(sent.encode('ascii'))

		ready = select.select([sock], [], [], 1)
		if ready[0]:
			recieved = str(sock.recv(1024), "utf-8")
			print(recieved)




#print("sent: {}".format(data))
#print("recv: {}".format(recieved))