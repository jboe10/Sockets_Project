import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

desktop_server_ip = '75.128.34.157'
desktop_port = 80

request = "GET / HTTP/1.1\nHost: "+desktop_server_ip+"\n\n"

s.connect((desktop_server_ip,desktop_port))
s.send(request.encode())
result = s.recv(4096)

#print(result)

while len(result) > 0:
	print(result)
	result = s.recv(4096)

