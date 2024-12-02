 '''TPRG 2131 Fall 2024 Assignment 2
 Chamath Kulathilaka (100889193)
 November 29, 2024
 This program is strictly my own work. Any material
 beyong course learning materials that is taken from
 the Web or other sources is properly cited, giving
 credit to original author (s).
 Following program acts as a client to recieve commands
 from a local server in RPi
'''
import socket
import os, time
import json

s = socket.socket()
address = '192.168.2.54' # Localclient
port = 5000
s.connect((address, port))


def main():
    jsonReceived = s.recv(1024)
    if jsonReceived == b'':
        print("Oop's")
        exit()
    data = json.loads(jsonReceived) # creates the JSON string
    # extracts, contents of the following items
    ret1 = data["volts"] 
    ret2 = data["temp-core"]
    ret3 = data["Memory"]
    ret4 = data["arm-memory"]
    ret5 = data["core-speed"]
    
    #prints the contents of the above extractions
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Bye...")
        exit()