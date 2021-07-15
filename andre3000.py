'''
Andre3000 Help page
Usage: python3 andre3000.py [-

-h Help page
-w Specify that the host system is windows*
-l Specify that the host system is linux*
-n Number repeated connections
-hc hop into a range of connections in a chronological list
-hr hop into a range of connections in a random list
-u username*
-p port (default is 22)
'''
helping_page="Usage: python3 andre3000.py [-w windows] [-l linux]  [-hc chrono order] " \
             "[-hr random order] [-n # of repeated connections] [-u username] [-p port]"
import os
import sys
import getpass
def Windows(payload):
    print("We are using Windows\n")
    payload.insert(0, "windows")
def Linux(payload):
    print("We are using linux\n")
    payload.insert(0,"linux")
def repeat(payload, value):
    print("You entered "+ sys.argv[value]+ " "+ sys.argv[value+1])
    payload.append(str(sys.argv[value+1]))
def chrono(payload):
    print("You entered chronological order")
    payload.append("chrono")
def random(payload):
    print("You entered random order")
    payload.append("random")
def username(payload, value):
    print("You entered "+ sys.argv[value]+ " "+ sys.argv[value+1])
    payload.append(str(sys.argv[value+1]))
def port(payload, value):
    print("You entered " + sys.argv[value] + " " + sys.argv[value + 1])
    payload.append(str(sys.argv[value + 1]))

def parameters(argument, value, payload):
    '''
    switcher = {
        "-w":Windows(payload),
        "-l":Linux(payload),
        "-n":repeat(payload, value),
        "-hc":chrono(payload),
        "-hr":random(payload),
        "-u":username(payload, value),
        "-p":port(payload, value)
    }
    switcher.get(argument)
    '''
    if argument == "-w": #Windows
        Windows(payload)
    elif argument == "-l": #Linux
        Linux(payload)
    elif argument == "-n": # Number of Repeats
        repeat(payload, value)
    elif argument == "-hc": # Chronological Order
        chrono(payload)
    elif argument == "-hr": # Random Order
        random(payload)
    elif argument == "-u": # Username
        username(payload, value)
    elif argument == "-p": # Port number
        port(payload, value)
    else:
        print("Incorrect Option")
payload = []
size = len(sys.argv)
print(size)
if size < 2:
    print(helping_page)
elif sys.argv[1] == "-h":
    print(helping_page)
else:
    for i in range (1, size):
        parameters(sys.argv[i], i, payload)

    hostname = getpass.getuser()
    print(getpass.getuser())
    if payload[0] == "windows":
        print("Preparing Config Files!")
        os.system("copy C:\\Users\\" + hostname + "\\.ssh\\config C:\\Users\\" + hostname + "\\.ssh\\config_old")
    elif payload[0] == "linux":
        path = "/home/"
        os.system("cp " + path + hostname + "/.ssh/config "+ hostname + "/.ssh/config_old")
    else:
        print("Somethings wrong, Please try again!")

    if payload[1] == "chrono":
        loop_time=payload[3]
        for i in range(0,loop_time):

print(payload)





#system = input("What Operating System are you on? ")
#if system == "windows" or system == "Windows":
#    print("You are on Windows, using copy and delete")
#if system == "linux" or system == "Linux":
#    print("You are using Linux, using cp and rm")

