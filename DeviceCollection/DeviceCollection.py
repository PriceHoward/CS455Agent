from os import cpu_count
from psutil import disk_usage, getloadavg, virtual_memory, net_io_counters,cpu_percent
import json
from uuid import uuid4
import time
#import network
import socket
from datetime import datetime

#from DeviceCollection.network import ConnectToServerSend

class DeviceCollection:
    def __init__(self):
        self.cpu_usage = 0.0
        self.memory_usage = 0
        self.disk_usage = 0
        self.network_usage = 0
        self.timeStamp = ""
    # Gets the CPU usage of the machine in the previous 15 minutes.
    def cpuusage(self):
        load1, load5, load15 = getloadavg()
        self.cpu_usage = (load1 / cpu_count())
        return cpu_percent()


    # Collects the total disk, used disk, and free disk.
    def diskusage(self):
        self.diskUsage = disk_usage("/")
        return self.diskUsage[3]

    # Takes the memory usage such as used, free, active, total.
    def memoryusage(self):
        self.memory_usage = virtual_memory()
        return self.memory_usage[2]

    # Return system-wide network I/O statistics as a named tuple.
    # TODO Rework the networkUsage to allow to find a percentage.
    def networkusage(self):
        self.network_usage = (net_io_counters().bytes_recv/net_io_counters().bytes_sent)
        return self.network_usage

    def timestamp(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time  

    def ConnectToServerSend(data):
        if data:
            _host = "45.79.202.234"
            _port = 8080
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((_host, _port))
            sock.sendall(data.encode('utf-8'))

    def jsonCreation(cpuStats, diskStats, memoryStats, networkStats, customID, timeStamp):
            dataString = {
                "ID": customID,
                "Time Stamp": timeStamp,
                "CPU": round(cpuStats),
                "DISK": round(diskStats),
                "MEMORY": round(memoryStats),
                "NETWORK": round(networkStats)
            }
            jsonData = json.dumps(dataString)
            print(jsonData)      
            return jsonData


    
    
def main():
    device = DeviceCollection
    customID = str(uuid4())
    while(True):
        data = device.jsonCreation(device.cpuusage(device), device.diskusage(device), device.memoryusage(device), device.networkusage(device), customID, device.timestamp(device))
        _host = "45.79.202.234"
        _port = 8080
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((_host, _port))
        sock.sendall(data.encode('utf-8'))
        time.sleep(5)
    
main()
