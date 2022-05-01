import pytest
from DeviceCollection import cpuusage, diskusage, memoryusage, networkusage, timestamp, jsonCreation

def test_cpuusage():
    assert int(cpuusage()) >= 0
    assert int(cpuusage()) < 100

def test_diskusage():
    disk = diskusage()
    assert disk >= 0
    assert disk <= 100

def test_memoryusage():
    memory = memoryusage()
    assert memory >= 0.0
    assert memory <= 100.0

def test_networkusage():
    network = networkusage()
    assert int(network[0]) >= 0
    assert int(network[1]) >= 0

def test_timestamp():
    assert timestamp() > 0

