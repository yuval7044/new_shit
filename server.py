import socket
from threading import Thread
server = socket.socket()
print("Socket succecfuly connected")
server.bind(('0.0.0.0', 5050))
clients_list = {}
print("Socket bindend to " + "5050")
server.listen(5)
#333

def new_clinet(c, addr, client_name):
    exit = False
    while exit == False:
        client_message = c.recv(4096).decode()
        if client_message == "":
            print(addr, "Disconnected")
            exit = True
        elif client_message == "ls":
            c.send(str(clients_list).encode())
        else:
            for name, computer in clients_list.items():
                if computer != c:
                    message = str(client_name) +  ": " + str(client_message)
                    computer.send(message.encode())

while True:
    clinet, add = server.accept()
    print("got connected from " + str(add))
    client_name = clinet.recv(1024).decode()
    clients_list.update({str(client_name) : clinet})
    client1 = Thread(target=new_clinet, args=(clinet,add,client_name))
    client1.start()
    print(clients_list)








