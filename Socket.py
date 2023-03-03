import socket

def python_server():
    host = socket.gethostname()
    port = 5050
    server_socket = socket.socket
    server_socket.bind((host,port))
    conn, address = server_socket.accept()
    print("thank you for connecting from:" + str(address))
    print ("1")

def python_client():
    host = socket.gethostname()
    port = 5050
    client_socket = socket.socket()
    client_socket.connect((host,port))

