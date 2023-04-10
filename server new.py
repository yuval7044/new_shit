import socket
from threading import Thread
s = socket.socket()
print("Socket succecfuly connected")
s.bind(('127.0.0.1', 5050))
clients_dict = {}
print("Socket bindend to " + "5050")
s.listen(5)

def new_client(c,addr,client_name, history):
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
            data = c.recv(1024).decode()
            clients_dict[name].append(client_name + " sent: "+ data)
        elif clients_terminal == "recv":
            new = "\n".join(clients_dict[client_name])
            c.send(new.encode())
        elif clients_terminal == "help" or clients_terminal == "Help":
            help = ("""[e]  - Exit \nls   - Client list \n send - send messages""")
            c.send(str(help).encode())
        elif clients_terminal == "notf":
            number = str(len(clients_dict[client_name]))
            c.send(("New " + number + " Messages").encode())
        elif clients_terminal == " ":
            Error = "commend not exist try help"
            c.send(str(Error).encode())
        elif clients_terminal == "":
            Error = "commend not exist try help"
            c.send(str(Error).encode())
        else:
            Error = "commend not exist try help"
            c.send(str(Error).encode())


def history_client_dict(key,value):
    clients_dict[key] = value


while True:
    c,add = s.accept()
    history = []
    print("Got connected from" + str(add))
    client_name = c.recv(1024).decode()
    history_client_dict(client_name, history)
    client1 = Thread(target=new_client, args=(c, add, client_name,history))
    client1.start()
