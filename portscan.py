from http import client
import socket

ports = [21,22,80,332,445,3306,25]
ip = input("Enter the IP or URL: ")
portsFound = False

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((ip, port))
    if code == 0:
        portsFound = True
        print(port, "OPEN")

if portsFound == False:
    print("We couldnt find any open port! :c")
