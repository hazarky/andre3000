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
import random
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
def randomset(payload):
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
            f.close()
            filesize = len(lines)
            f = open("C:\\Users\\" + getpass.getuser() + "\\.ssh\\config", "w")
            f.write("Host andre0\n\tHostname " + lines[0] + "\n\tUser " + payload[5] + "\n\tPort " + payload[6] + "\n")
            j=0
            for i in range(1,int(timeloop)*filesize):
                if j == filesize:
                    j=0
                f.write("Host andre"+str(i)+"\n\tHostname "+lines[j]+ "\n\tUser "+ payload[5] + "\n\tPort "+ payload[6]
                        +"\n\tProxyCommand ssh.exe -q -W %h:%p andre"+ str(i-1)+"\n")
                j=j+1
            f.close()
            print("ssh config is configured. To start, type: ssh andre" + str((int(timeloop)*filesize - 1)))
    else: #random order
        '''
        This is difficult. We need a random number generator that only repeats the number one time.
        Given a range of pre-determined numbers the generator must generate a random number from that range
        without repeating more than once. These numbers will be used to connect together in the list and will provide
        a "random" path that the connection is coming from.
        Two Solutions: Patient Zero or Duplicates 
        Patient Zero: All connections are connected and are traced back to andre0 (hardcoded list)
        Duplicate: all connections are on the random field and is up to the generator to make a list (randomly created)
        '''
        if payload[3] == "-a": #single address
            timeloop=payload[2]
            f = open("C:\\Users\\" + getpass.getuser() + "\\.ssh\\config", "w")
            f.write("Host andre0\n\tHostname " + payload[4] + "\n\tUser " + payload[5] + "\n\tPort " + payload[6] + "\n")
            i=0
            entrylist=[0] #necessary or it hangs
            while len(entrylist) < int(timeloop): # This uses patient Zero version since its one address
                entry = random.randrange(1,int(timeloop))
                print("Setting up entry #"+ str(len(entrylist)))
                if search(entrylist, entry) != True:
                    if i==0:
                        f.write("Host andre" + str(entry) + "\n\tHostname " + payload[4] + "\n\tUser " + payload[
                            5] + "\n\tPort " + payload[6]+ "\n\tProxyCommand ssh.exe -q -W %h:%p andre0\n")
                        i=i+1
                        entrylist.append(entry)
                    else:
                        f.write("Host andre" + str(entry) + "\n\tHostname " + payload[4] + "\n\tUser " + payload[
                            5] + "\n\tPort " + payload[6] + "\n\tProxyCommand ssh.exe -q -W %h:%p andre"+str(len(entrylist)-1)+"\n")
                        entrylist.append(entry)
                        i=i+1
            f.close()
            entrylist.clear()
        else: #payload[3] =="-A":
            timeloop=payload[2]
            f = open(payload[4], "r")
            lines = f.readlines()
            f.close()
            filesize = len(lines)
            connections = timeloop*filesize
            f = open("C:\\Users\\" + getpass.getuser() + "\\.ssh\\config", "w")
            i=0
            entrylist=[]
            proxentrylist=[]
            while len(entrylist) < int(connections):
                entry = random.randrange(0, int(connections))
                proxentry = random.randrange(0, int(connections))
                print("Setting up entry #" + str(len(entrylist)))
                if search(entrylist, entry) != True and search(proxentrylist,proxentry) !=True:
                    if i < filesize:
                        if random.randrange(0,5) < 1: #20% chance
                            f.write("Host andre" + str(entry) + "\n\tHostname " + lines[i] + "\n\tUser " + payload[
                                5] + "\n\tPort " + payload[6] +"\n")
                            i=i+1
                            entrylist.append(entry)
                        else:
                            f.write("Host andre" + str(entry) + "\n\tHostname " + lines[i] + "\n\tUser " + payload[
                                5] + "\n\tPort " + payload[6] + "\n\tProxyCommand ssh.exe -q -W %h:%p andre" +
                                                str(proxentry) + "\n")
                            i=i+1
                            entrylist.append(entry)
                            proxentrylist.append(entry)
                    else:
                        i = 0






def search(list, entry):
    for i in range (len(list)):
        if list[i] == entry:
            return True
    return False

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
        randomset(payload)
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
print(payload)
