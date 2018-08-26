import socket
import threading

class msg:

    def __init__(self, msg, from_address):
        self.msg = msg
        self.from_address = from_address


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = "localhost"
        self.port = port
        self.client_list = []
        self.msg_queue = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            self.client_list.append(client)
            print("got connection from" + str(address))
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):

        # Append client address to list of current clients
       

        # set the response to echo back data about client
        size = 1024
        response = "username = " + str(address[1])
        client.send(response.encode('ascii'))
        print("Username assigned")

        # spin recieveing message and add to msg que
        recieved = ""
        while recieved != "exit()":

            # Take in messages from all clients and add to msg_queue
            recieved = str(client.recv(1024), "utf-8")
            messge = msg(recieved, address)
            self.msg_queue.append(messge)

            # Print Message to server Console
            print(str(address[1]) + ": " +recieved)

            #Broadcast message back to all clients
            self.broadcast_msg(client)

        #remove client from client list then close client
        client.close()

        print(self.client_list)
        while self.msg_queue:
            pop = self.msg_queue.pop(0)
            print(pop.msg)



    def broadcast_msg(self, client):
        while self.msg_queue:
            pop = self.msg_queue.pop(0)
            for i in range(0,len(self.client_list)):
                if self.client_list[i] != client:
                    message = str(pop.from_address) + ": " + pop.msg + "\n"
                    self.client_list[i].send(message.encode('ascii'))



if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()