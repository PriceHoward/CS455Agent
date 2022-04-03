from os import cpu_count
from textwrap import indent
from turtle import end_fill
from psutil import disk_usage, getloadavg, virtual_memory, net_io_counters
import json
import sys


# Gets the CPU usage of the machine in the previous 15 minutes.
def cpuusage():
    load1, load5, load15 = getloadavg()
    cpu_usage = (load15 / cpu_count()) * 100
    return cpu_usage

# Collects the total disk, used disk, and free disk.
def diskusage():
    diskUsage = disk_usage("/")
    return diskUsage[3]
# Takes the memory usage such as used, free, active, total.
def memoryusage():
    memory_usage = virtual_memory()
    return memory_usage[2]

# Return system-wide network I/O statistics as a named tuple.
#TODO Rework the networkUsage to allow to find a percentage.
def networkusage():
    network_usage = (net_io_counters().bytes_recv - net_io_counters().bytes_sent) / 100000000
    return network_usage

def jsonCreation(cpuStats, diskStats, memoryStats, networkStats):
        dataString = {
            "CPU": cpuStats,
            "DISK": diskStats,
            "MEMORY": memoryStats,
            "NETWORK": networkStats
        }
        print(json.dumps(dataString))
        
def main():
    cpuStats = cpuusage()
    diskStats = diskusage()
    memoryStats = memoryusage()
    networkStats = networkusage()
    jsonCreation(cpuStats, diskStats, memoryStats, networkStats)


main()
