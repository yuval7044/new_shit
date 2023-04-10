import socket
import time
from threading import Thread
s = socket.socket()
s.connect(("127.0.0.1", 5050))
print( "Connected to 127.0.0.1 at Port 5050")
Name = input(str("Name: "))
s.send(Name.encode())

def sending_message():
    while True:
        message = input(str("Terminal: "))

        s.send(str(message).encode())

        if message == "send":
            name = input("Who to send?")
            s.send(str(name).encode())
            message = input("Message to " + name + ":")
            s.send(str(message).encode())
        elif message == "recv":
            time.sleep(0.5)
        time.sleep(0.1)

        if message == "[e]":
            break

#asdsa



def receiving_message():
    while True:
        data = s.recv(4096).decode()
        print(data)
        if data == "GoodBye :D":
            break

sending = Thread(target=sending_message)
receiving = Thread(target=receiving_message)
sending.start()
receiving.start()