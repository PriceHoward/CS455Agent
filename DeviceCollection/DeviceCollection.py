from os import cpu_count
from textwrap import indent
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
def networkusage():
    network_usage = (net_io_counters().bytes_recv - net_io_counters().bytes_sent) / 100
    return network_usage

# Input everything into a file as a json.
def fileCreation(cpuStats, diskStats, memoryStats, networkStats):
    with open('agent.json', 'w') as json_file:
        json.dump({'CPU' : round(cpuStats)}, json_file)
        json_file.write("\n")
        json.dump({'DISK' : round(diskStats)}, json_file)
        json_file.write("\n")
        json.dump({'MEMORY' : round(memoryStats)}, json_file)
        json_file.write("\n")
        json.dump({'NETWORK' : round(networkStats)}, json_file)
        json_file.close()


def main():
    cpuStats = cpuusage()
    diskStats = diskusage()
    memoryStats = memoryusage()
    networkStats = networkusage()
    fileCreation(cpuStats, diskStats, memoryStats, networkStats)
    cpuStats = cpuusage()
    diskStats = diskusage()
    memoryStats = memoryusage()
    networkStats = networkusage()
    fileCreation(cpuStats, diskStats, memoryStats, networkStats)


main()
