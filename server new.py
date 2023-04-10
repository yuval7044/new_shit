import socket
from threading import Thread
s = socket.socket()
print("Socket succecfuly connected")
s.bind(('127.0.0.1', 5050))
clients_dict = {}
print("Socket bindend to " + "5050")
s.listen(5)





def new_client(c,addr,client_name):
    while True:
        clients_terminal = c.recv(1024).decode()
        if clients_terminal == "[e]":
            print(addr, "Disconnected")
            bye = "GoodBye :D"
            c.send(str(bye).encode())
            clients_dict.pop(client_name)
            break
        elif clients_terminal == "ls":
            names = str(clients_dict.keys())
            c.send(str(names).encode())
        elif clients_terminal == "send":
            name = c.recv(1024).decode()
            print(clients_dict[name])
            data = c.recv(1024).decode()
            print(clients_dict[name])
            clients_dict[name].send(str(data).encode())

        elif clients_terminal == "help":
            help = ("""[e]  - Exit
ls   - Client list
send - send messages""")
            c.send(str(help).encode())

        elif clients_terminal == " ":
            Error = "commend not exist try help"
            c.send(str(Error).encode())
        elif clients_terminal == "":
            Error = "commend not exist try help"
            c.send(str(Error).encode())
        else:
            Error = "commend not exist try help"
            c.send(str(Error).encode())


def add_client_dict(key,value):
    clients_dict[key] = value


while True:
    c,add = s.accept()
    print("Got connected from" + str(add))
    client_name = c.recv(1024).decode()
    add_client_dict(client_name, c)
    client1 = Thread(target=new_client, args=(c, add, client_name))
    client1.start()
