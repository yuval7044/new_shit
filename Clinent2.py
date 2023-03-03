import socket
message = ""
s = socket.socket()
s.connect(("127.0.0.1", 5050))
print("Connected to 127.0.0.1 at Port 5050")
Name = input(str("Name: "))
s.send(Name.encode())
while True:
    message = input(str("message:"))
    if message == "[e]":
        break
    elif message == "ls":
        s.send(message.encode())
        print("Clients Connected: ")
        print(s.recv(1024).decode())
    else:
        s.send(message.encode())
        data = s.recv(1024).decode()
        print("message from server:", data)
