import socket
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Successfully created")

port = 9999


server_socket.bind((socket.gethostname(), port))
print ("socket binded to " + str(port))


# Put the socket into listening mode
server_socket.listen(5)
print ("socket is listening")

# making our connections non blocking
server_socket.setblocking(0)
server_socket.settimeout(30)

# our threads
threads = []

# loop till we shut down server or error
while True:

	# Establish connection with client.
	(client_socket, addr) = server_socket.accept()
	print ("got connection from  " + str(addr))

	
	# send a thank you msg to the client.
	msg = 'thanks for connecting, type "exit()" to close connection'
	client_socket.send(msg.encode('ascii'))
	recv_msg_auth = ""


	"""
	while recv_msg_auth != "exit()":
		recv_msg = client_socket.recv(1024)
		recv_msg_auth = recv_msg.decode('ascii')
		print(recv_msg_auth)
	"""
	threads.append(client_socket)

	print(threads)

	while recv_msg_auth != "exit()":
		recv_msg = client_socket.recv(1024)
		recv_msg_auth = recv_msg.decode('ascii')
		print(recv_msg_auth)

	print("socket closed")
	client_socket.close()
	threads.remove(client_socket)
