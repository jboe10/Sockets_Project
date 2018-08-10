import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 9999


# connect to the server on local computer
s.connect((host, port))

# receive data from the server
msg = s.recv(1024)
print(msg.decode('ascii'))

var = ""
while var != "exit()":
	var = input(': ')
	s.send(var.encode('ascii'))


# close the connection
s.close()