from os import cpu_count
from psutil import disk_usage, getloadavg, virtual_memory, net_io_counters,cpu_percent
import json
from uuid import uuid4
import time
import network

class DeviceCollection:
    def __init__(self):
        self.cpu_usage = 0.0
        self.memory_usage = 0
        self.disk_usage = 0
        self.network_usage = 0

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

    def jsonCreation(cpuStats, diskStats, memoryStats, networkStats, customID):
            dataString = {
                "ID": customID,
                "CPU": round(cpuStats),
                "DISK": round(diskStats),
                "MEMORY": round(memoryStats),
                "NETWORK": round(networkStats)
            }
            jsonData = json.dumps(dataString)
            print(jsonData)
            network.ConnectToServerSend(jsonData)
            
    
def main():
    device = DeviceCollection
    customID = str(uuid4())
    while(True):
        device.jsonCreation(device.cpuusage(device), device.diskusage(device), device.memoryusage(device), device.networkusage(device), customID)
        time.sleep(5)
    
main()
