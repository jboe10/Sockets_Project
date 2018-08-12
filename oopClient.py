import socket 
import sys

HOST, PORT = "localhost", 9999


#create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	# connect to server and send data
	sock.connect((HOST, PORT))

	# Recieve data from the server and assign user name
	sent = ""
	recieved = str(sock.recv(1024), "utf-8")
	print("recv: {}".format(recieved))
	username = recieved[11:]

	# Join message client side
	print(username + " new user")
	
	# spin up chat 
	while sent != "exit()":
		sent = input(": ")
		sock.send(sent.encode('ascii'))

		try:
			recieved = str(sock.recv(1024), "utf-8")
			print(recieved)
			break
		except socket.error:
			x = 1




#print("sent: {}".format(data))
#print("recv: {}".format(recieved))