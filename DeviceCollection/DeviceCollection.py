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


"""def readmeCreation():
    # Building a README to be sent with the json File.
    with open("../Json Files/README.txt", 'w') as read:
        read.write("What is in the json File?\nThe first line is the CPU usage over 15 minutes of being used.\n")
        read.write("The second line is the Disk usage split as: Total Disk, Used Disk, Free Disk, Percentage used.\n")
        read.write("The third line is Memory Usage slit as: Total Memory, Availabale Memory, Percent Used, Used, Free, "
                   "Active, Inactive, Wired.\nThe fourth line is Network Usage split as: Bytes_Sent, Bytes_Recieved,"
                   "Packets_Sent, Packets_Recieved, Errin, Errout, Dropin, Dropout\n")
        read.close()
"""


def main():
    cpuStats = cpuusage()
    diskStats = diskusage()
    memoryStats = memoryusage()
    networkStats = networkusage()
    fileCreation(cpuStats, diskStats, memoryStats, networkStats)
    #readmeCreation()


main()
