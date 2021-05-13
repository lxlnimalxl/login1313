import socket

c = ('localhost' , 12345)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(c)

#data = client.recv(1024)

#print data
while True:
    data = client.recv(1024)
