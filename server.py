import socket
from threading import Thread
s = socket.socket()
print("Socket succecfuly connected")
s.bind(('127.0.0.1', 5050))
clients_dict = {}
print("Socket bindend to " + "5050")
s.listen(5)

def dict_value(dict, addr): #print the place of speceific value in dict
    for value in dict.values():
        if value == addr:
            return len(addr)

def dict_keys(dict, client): #print the place of speceific key in dict
    for name in dict:
        if name == client:
            return len(client)

def new_clinet(c, addr):
    name_of_client = ""
    exit = False
    place_of_ip = dict_value(clients_dict,addr)
    place_of_name = dict_keys(clients_dict,client_name)
    while exit == False:
        client_message = c.recv(4096).decode()
        if client_message == "":
            print(addr, "Disconnected")
            exit = True
        elif client_message == "ls":
            c.send(str(clients_dict).encode())
        else:
            print(name_of_client,"--> ",client_message)
            c.send(client_message.encode())

def add_client_dict(key,value):
    clients_dict[key] = value

while True:
    c, add = s.accept()
    print("got connected from " + str(add))
    client_name = c.recv(1024).decode()
    add_client_dict(client_name,add)
    client1 = Thread(target=new_clinet, args=(c,add))
    client1.start()
    print(clients_dict)


