import socket
IPADDR = "localhost"
PORT = 4483
# receive 4096 bytes each time
BUFFER_SIZE = 4096
while(True):
    s = socket.socket()
    s.bind((IPADDR, PORT))
    s.listen(5)
    print(f"[*] Listening as {IPADDR}:{PORT}")
    client_socket, address = s.accept()
    if(client_socket):
        print(f"[+] {address} is connected.")

        received = client_socket.recv(BUFFER_SIZE).decode()
        # start receiving the file from the socket
        print(received)

        # close the client socket
        client_socket.close()
        # close the server socket
    s.close()
