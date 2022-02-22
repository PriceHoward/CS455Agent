import os
import psutil
import json


# Collects the total disk, used disk, and free disk.
def diskusage():
    return psutil.disk_usage("/")


# Gets the CPU usage of the machine in the previous 15 minutes.
def cpuusage():
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load15 / os.cpu_count()) * 100
    return cpu_usage


# Takes the memory usage such as used, free, active, total.
def memoryusage():
    return psutil.virtual_memory()


# Return system-wide network I/O statistics as a named tuple.
def networkusage():
    return psutil.net_io_counters(pernic=False, nowrap=True)


# Input everything into a file as a json.
def fileCreation(cpuStats, diskStats, memoryStats, networkStats):
    with open('agent.json', 'w') as json_file:
        json.dump(cpuStats, json_file)
        json_file.write("\n")
        json.dump(diskStats, json_file)
        json_file.write("\n")
        json.dump(memoryStats, json_file)
        json_file.write("\n")
        json.dump(networkStats, json_file)
        json_file.close()


def main():
    cpuStats = cpuusage()
    diskStats = diskusage()
    memoryStats = memoryusage()
    networkStats = networkusage()
    fileCreation(cpuStats, diskStats, memoryStats, networkStats)
    #readmeCreation()


main()
