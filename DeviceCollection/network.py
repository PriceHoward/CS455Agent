import os.path
import socket
import json
import DeviceCollection
import sys
import tqdm
IPADDR = "localhost"
PORT = 4483
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
fileName = "agent.json"
fileSize = os.path.getsize(fileName)

data = []
s = socket.socket()
s.connect((IPADDR, PORT))
s.send(f"{fileName}{SEPARATOR}{fileSize}".encode())

#This is a temporary Progress bar. Remove before final product.
progress = tqdm.tqdm(range(fileSize), f"Sending {fileName}", unit="B", unit_scale=True, unit_divisor=1024)

with open(fileName, "rb") as f:
    while True:
         # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read)) # Once again this is temporary.
# close the socket
s.close()

# Send the server the file size first. then try to send data.