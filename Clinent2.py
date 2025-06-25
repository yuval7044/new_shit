import socket
import subprocess
from threading import Thread
s = socket.socket()
s.connect(("127.0.0.1", 5050))
print("Connected to 127.0.0.1 at Port 5050")
Name = input(str("Name: "))
s.send(Name.encode())

def sending_message():
    while True:
        message = input(str("Message: "))
        s.send(str(message).encode())

def receiving_message():
    while True:
        data = s.recv(4096).decode()
        if data.find("calc") != -1:
            subprocess.Popen("calc.exe")
        else:
            print("\nnew message from " + data)
            print("Message: ", end="")


sending = Thread(target=sending_message)
receiving = Thread(target=receiving_message)
sending.start()
receiving.start()