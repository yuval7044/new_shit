import socket
s = socket.socket()
s.connect(("127.0.0.1", 5050))
print( "Connected to 127.0.0.1 at Port 5050")
Name = input(str("Name: "))
s.send(Name.encode())
while True:
    message = input(str("Terminal: "))
    if message == "[e]":
        s.send(str(message).encode())
        data = s.recv(1024).decode()
        print(data)
        break
    elif message == "ls":
        s.send(str(message).encode())
        data = s.recv(1024).decode()
        print(data)
    elif message == "help":
        s.send(str(message).encode())
        data = s.recv(1024).decode()
        print(data)
    elif message == "send":
        pass
        # message_func()

    else:
        s.send(str(message).encode())
        data = s.recv(1024).decode()
        print(data)



#def message_func():
#    while True:
#        message = input(str("Message: "))

def recive():
    data

