import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		# self.request is TCPsocket connected to client
		#self.data = self.request.recv(1024).strip()
		#print("{} wrote: ".format(self.client_address[0]))
		#print(self.data)
		
		# send connection message to chat Server
		msg = 'Connection to Chat Server established, WELCOME'
		self.request.send(msg.encode('ascii'))

		# now we loop the conncetion till the client wants to exit()
		recv_msg_auth = ""
		while recv_msg_auth != "exit()":
			recv_msg_auth = self.request.recv(1024)
			print(recv_msg_auth)


		# just send back the same data but uppercased
		#self.request.sendall(self.data.upper())


if __name__ == "__main__":

	HOST, PORT = "localhost", 9999


	# create the server binding to localhost on port 9999
	with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
		# Activate the server
		# interrupt with ctr-c
		server.serve_forever()