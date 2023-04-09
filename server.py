import socket
from threading import Thread
s = socket.socket()
print("Socket succecfuly connected")
s.bind(('127.0.0.1', 5050))
clients_dict = {}
print("Socket bindend to " + "5050")
s.listen(5)

while True:
    c, add = s.accept()
    print("got connected from " + str(add))
    client_name = c.recv(1024).decode()
    add_client_dict(client_name,add)
    client1 = Thread(target=new_clinet, args=(c,add))
    client1.start()
    print(clients_dict)



def new_clinet(c, addr):
    name_of_client = ""
    exit = False
    while exit == False:
        client_message = c.recv(4096).decode()
        if client_message == "":
            print(addr, "Disconnected")
            exit = True
        elif client_message == "ls"
            c.send(str(clients_dict).encode())
        else:
            print(name_of_client,"--> ",client_message)
            c.send(client_message.encode())

def add_client_dict(key,value):
    clients_dict[key] = value




