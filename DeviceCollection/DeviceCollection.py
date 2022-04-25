from os import cpu_count
from os.path import exists
from psutil import disk_usage, getloadavg, virtual_memory, net_io_counters, cpu_percent
from json import dumps
from uuid import uuid4
import time
from socket import socket, AF_INET, SOCK_STREAM
import logging


    # Gets the CPU usage of the machine in the previous 15 minutes.
def cpuusage():
    load1, load5, load15 = getloadavg()
    cpu_usage = (load1 / cpu_count())
    return cpu_percent()


    # Collects the total disk, used disk, and free disk.
def diskusage():
    diskUsage = disk_usage("/")
    return diskUsage[3]

    # Takes the memory usage such as used, free, active, total.
def memoryusage():
    memory_usage = virtual_memory()
    return memory_usage[2]

    # Return system-wide network I/O statistics as a named tuple.
    # TODO Rework the networkUsage to allow to find a percentage.
def networkusage():
    network_usage = net_io_counters()
    return network_usage

def timestamp():
    return int(time.time())

def ConnectToServerSend(data):
    _host = "cs.csis.work"
    _port = 8080
    if data:
        for i in range(0,3):
            try:
                sock = socket(AF_INET, SOCK_STREAM)
                sock.connect((_host, _port))
                sock.sendall(data.encode('utf-8'))
                time.sleep(5)
                return True
                
            except:
                logging.error(" Socket Error. Cannot Connect. Retry #%i", i + 1)
                sock.close()
                if i == 2:
                    logging.warning(" Agent Could not connect. Starting Shutdown.")
                    return False
            time.sleep(10)

#Creates JSON data to send over the socket.
def jsonCreation(cpuStats, diskStats, memoryStats, networkStats, customID, timeStamp):
        dataString = {
            "ID": customID,
            "Time Stamp": timeStamp,
            "CPU": round(cpuStats),
            "DISK": round(diskStats),
            "MEMORY": round(memoryStats),
            "NETWORK" :
            {
                "BYTES SENT": networkStats[0],
                "BYTES RECEIVED":  networkStats[1]
            }
        }
        jsonData = dumps(dataString)     
        return jsonData
    
def checkForUUID():
    if exists('uuid.txt'):
        with open('uuid.txt', 'r') as file:
            for readline in file:
                return readline.strip()
        file.close()
    else:
        customID = str(uuid4())
        file = open('uuid.txt', 'w')
        file.write(customID)
        file.close()
        return customID
 
def main():
    customID = checkForUUID()
    shutdown = True
    while True:
        if shutdown == True:
            shutdown = ConnectToServerSend(jsonCreation(cpuusage(), diskusage(), memoryusage(), networkusage(), customID, timestamp()))
        else:
            logging.error(" Agent is Shutting Down. Please Restart.")
            break
main()
