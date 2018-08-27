import socket 
import sys
import select
import threading

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from chatUI import Ui_MainWindow

HOST, PORT = "localhost", 9999

class AppWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(AppWindow, self).__init__()
		self.setupUi(self)

		self.client = None
		self.connected = False


		##################### Button Click Actions ####################

		# Send Message to Server
		self.sendBtn.clicked.connect(self.send_Action)
		
		# Connect to server
		self.connectButton.clicked.connect(self.connect_Action)

		# Disconnect Button
		self.disconnectButton.clicked.connect(self.disconnect)


	##################### Function Declartaions #######################

	#connect button
	def connect_Action(self):
		self.client = Threaded_Client() # spin up client
		self.connected = True
		self.client.chatroom(self)

		# Signal user has connected
		self.listWidget.addItem("[SERVER: User " +self.client.username + " has joined]")

		#check for messages in the initial queue
		#self.client.chat_out()

		# recursivly look for messages to print to listWidget
		#self._connect_Action()

	def _connect_Action(self):
		if self.client.recieved_q == []:
			self._connect_Action()
		else:
			self.print_recv_msgs()


		# empty recv q -> look for more msgs
		# full recv q? print it out to widget

	#send button
	def send_Action(self):
		
		text = self.lineEdit.text() # Get the value of lineEdit
		self.lineEdit.clear()       # Clear the Text

		self.client.chat_send(text, self) # Send message to outgoing message q




	def addItem(self):
		value = str("[User " + str(self.lineEdit.text()) + " has Joined]")
		self.lineEdit.clear()
		self.listWidget.addItem(value)


	#disconnect button
	def disconnect(self):
		self.connected = False

	def print_recv_msgs(self):
		while self.client.recieved_q:
			pop = self.client.recieved_q.pop(0)
			self.listWidget.addItem(pop)



	#send button



class Threaded_Client(object):

	def __init__(self):
		self.host = HOST
		self.port = PORT
		self.username = None
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.host, self.port))
	
		self.recieved_q = []
		self.send_q =     []


	def chatroom(self, obj):
		ready = select.select([self.sock],[],[],1)
		if ready[0]:
			recieved = str(self.sock.recv(1024), "utf-8")
			print("recv: {}".format(recieved))
			self.username = recieved[11:]



		#print(str(self.username) + "new user")

		#threadnig.Thread(target = self.chat_in)
		#self.chat_out(obj)

	def chat_send(self, text, gui):
		self.sock.send(text.encode('ascii'))

		#ready = select.select([self.sock], [], [], 1)
		#if ready[0]:
		recieved = str(self.sock.recv(1024), "utf-8")
		print(recieved)
		self.recieved_q.append(recieved)
		gui.print_recv_msgs()
		
		#self.send_q.append(text)

	def chat_out(self, obj):
		print("made thread")
		exit_Detected = False

			# Check for messages sent from server
			

		while self.send_q:
			pop = self.send_q.pop(0)

			if pop == "exit()":
				exit_Detected = True

			self.sock.send(pop.encode('ascii'))

			"""
			ready = select.select([self.sock], [], [], 1)
			if ready[0]:
				recieved = str(self.sock.recv(1024), "utf-8")
				print(recieved)
				self.recieved_q.append(recieved)
				obj.print_recv_msgs()
			"""


if __name__ == "__main__":

	"""
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()

	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)

	MainWindow.show()
	sys.exit(app.exec_())
	"""
	app = QtWidgets.QApplication(sys.argv)
	widget = AppWindow()
	widget.show()
	sys.exit(app.exec_())