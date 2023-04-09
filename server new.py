import socket
from myfunctions import add_client_dict
from threading import Thread
s = socket.socket()
print("Socket succecfuly connected")
s.bind(('127.0.0.1', 5050))
clients_dict = {}
print("Socket bindend to " + "5050")
s.listen(5)





def new_client(c,addr):
    out = False
    names = str(clients_dict.keys())
    while out == False:
        clients_terminal = c.recv(1024).decode()
        print(clients_terminal)
        if clients_terminal == "[e]":
            print(addr, "Disconnected")
            bye = "GoodBye :D"
            c.send(str(bye).encode())
            out = True
        elif clients_terminal == "ls":
            c.send(str(names[9:]).encode())
        elif clients_terminal == "send":
            name = c.recv(1024).decode()
            for ign in clients_dict.keys():
                if ign == name:
                    data = s.recv(4096)

                else:
                    Error = "Error Name not found try ls"
                    c.send(Error.encode())

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
    add_client_dict(client_name, add)
    client1 = Thread(target=new_client, args=(c, add))
    client1.start()
