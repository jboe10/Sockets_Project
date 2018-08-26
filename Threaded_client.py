import socket 
import sys
import select
import threading

HOST, PORT = "localhost", 9999

class Threaded_Client(object):

	def __init__(self):
		self.host = HOST
		self.port = PORT
		self.username = None
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connet(self.host, self.port)
		self.sock.setblocking(0)


	def chatroom(self):	
		ready = select.select([self.sock],[],[],1)
		if ready[0]:
			recieved = str(self.sock.recv(1024), "utf-8")
			print("recv: {}".format(recieved))
		self.username = recieved[11:]


		print(self.username + "new user")

		threadnig.Thread(target = self.chat_in)
		threading.Thread(target = self.chat_out)

	def chat_in(self):
		sent = input(": ")
		self.sock.send(sent.encode('ascii'))

	def chat_out(self):
		ready = select.select([self.sock], [], [], 1)
		if ready[0]:
			recieved = str(self.sock.recv(1024), "utf-8")
			print(recieved)


if __name__ == "__main__":

	Threaded_Client().chatroom()