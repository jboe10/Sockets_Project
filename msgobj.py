class msg:

    def __init__(self, msg, from_address):
        self.msg = msg
        self.from_address = from_address

queue = []

msgs = input("msg: ")
add = input("add: ")

message = msg(msgs, add)

queue.append(message)

msgs = input("msg: ")
add = input("add: ")

message = msg(msgs, add)

queue.append(message)

msgs = input("msg: ")
add = input("add: ")

message = msg(msgs, add)

queue.append(message)

msgs = input("msg: ")
add = input("add: ")

message = msg(msgs, add)

queue.append(message)

msgs = input("msg: ")
add = input("add: ")

message = msg(msgs, add)

queue.append(message)

while queue:
	pop = queue.pop(0)
	print(pop.msg + " " + pop.from_address)
