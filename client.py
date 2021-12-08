import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',1234))
a = input("arp or rarp:")
if a=="ARP" or a=="arp":
    add = input("enter ip:")
elif a=="rarp" or a=="RARP":
    add = input('enter mac:')
s.send(add.encode())
mac = s.recv(2048)
mac = mac.decode("utf-8")
if a=="ARP" or a=="arp":
    print("mac of",add,'is:',mac)
else:
    print("IP of",add,"is:",mac)