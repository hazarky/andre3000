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
help_page="Usage: python3 andre3000.py [-w windows] [-l linux]  [-hc chrono order] " \
             "[-hr random order] [-n # of repeated connections] -a [address] -A[address file]" \
          "[-u username] [-p port]"
examples="python3 andre3000.py -w -hc -n 10 -a 10.10.10.180 -u user1 -p 22\n" \
         "python3 andre3000.py -l -hr -n 50 -A newyork.txt -u user3 -p 22\n" \
         "python3 andre3000.py -w -hr -n 3000 -A webservers.txt -u admin -p 2222"
import os
import sys
import getpass
def Windows(payload):
    print("We are using Windows\n")
    payload.insert(0, "windows")
    hostname = getpass.getuser()
    print("Preparing Config Files!")
    os.system("copy C:\\Users\\" + hostname + "\\.ssh\\config C:\\Users\\" + hostname + "\\.ssh\\config_old")
def Linux(payload):
    print("We are using linux\n")
    payload.insert(0,"linux")
    hostname = getpass.getuser()
    print("Preparing Config Files!")
    path = "/home/"
    os.system("cp " + path + hostname + "/.ssh/config " + hostname + "/.ssh/config_old")
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
    print(value+1)
    payload.append(str(sys.argv[value+1]))
def port(payload, value):
    print("You entered " + sys.argv[value] + " " + sys.argv[value + 1])
    payload.append(str(sys.argv[value + 1]))
def address(payload, value):
    print("You entered " + sys.argv[value] + " " + sys.argv[value + 1])
    payload.append(sys.argv[value])
    payload.append(str(sys.argv[value+1]))
def listaddress(payload, value):
    print("You entered " + sys.argv[value] + " " + sys.argv[value + 1])
    payload.append(sys.argv[value])
    payload.append(str(sys.argv[value+1]))
def obby_type(payload):
    print(payload[1])
    if payload[1] == "chrono": #chronological
        print("You are using chronological")
        if payload[3] == "-a": #single address
            timeloop=payload[2]
            f=open("C:\\Users\\"+getpass.getuser()+"\\.ssh\\config", "w")
            f.write("Host andre0\n\tHostname "+ payload[4]+"\n\tUser "+payload[5]+"\n\tPort "+payload[6]+"\n")
            for i in range(1,int(timeloop)):
                f.write("Host andre"+str(i)+"\n\tHostname "+payload[4]+"\n\tUser "+ payload[5]+"\n\tPort "+payload[6]
                        +"\n\tProxyCommand ssh.exe -q -W %h:%p andre"+str(i-1)+"\n")
            f.close()
            print("ssh config is configured. To start, type: ssh andre"+str((int(timeloop)-1)))
        else: #payload[3] == "-A"
            timeloop=payload[2]
            f = open(payload[4], "r")
            lines = f.readlines()
            filesize = len(lines)
            f = open("C:\\Users\\" + getpass.getuser() + "\\.ssh\\config", "w")
            f.write("Host andre0\n\tHostname " + lines[0]+ "\n\tUser " + payload[5] + "\n\tPort " + payload[6] + "\n")
            for i in range(1,int(timeloop)*filesize):








    else:#random order
        print("You are using random")

def parameters(argument, value, payload):
    if argument == "-w": #Windows
        Windows(payload)
    elif argument == "-l": #Linux
        Linux(payload)
    elif argument == "-n": # Number of Repeats
        repeat(payload, value)
    elif argument == "-a":#one address
        address(payload, value)
    elif argument == "-A": #multiple addresses
        listaddress(payload, value)
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
    print(help_page)
    print(examples)
elif sys.argv[1] == "-h":
    print(help_page)
    print(examples)
else:
    for i in range (1, size):
        parameters(sys.argv[i], i, payload)
    obby_type(payload)

#        if payload
        #f.write("Host andre0\n\tHostname 192.168.181.128\n\tUser kali\n\tPort 22\n")
        #for i in range(0,loop_time):

print(payload)
