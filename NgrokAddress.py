import subprocess

def GetAddress(command):
    output = subprocess.getoutput(command)
    return output