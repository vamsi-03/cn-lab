import socket

table={
    '192.168.1.1' : '1E.4A.4A.11',
    '192.168.2.1' : '5E.51.4B.01',
    '192.168.1.3' : '4B.35.CD.32',
    '192.168.4.1' : 'AF.4D.1F.FF'
}

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(('',1234))
s.listen(4)
clientsocket,address = s.accept()
print("connectfrom",address,"hash established")
ip = clientsocket.recv(1024)
ip = ip.decode("utf-8")
mac = table.get(ip,'no entry for given address')
clientsocket.send(mac.encode())
