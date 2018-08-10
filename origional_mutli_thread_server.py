import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = "localhost"
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print("got connection from" + str(address))
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024

        #assign a username based on the address
        data = "username = " + str(address[1])
        response = data
        client.send(response.encode('ascii'))
        print("Username assigned")

        # if we receive a client exit message, exit
        recieved = ""
        while recieved != "exit()":
            recieved = str(client.recv(1024), "utf-8")
            print(str(address[1]) + ": " +recieved)
        client.close()


if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()