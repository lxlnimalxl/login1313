import socket

s = ('localhost' , 12345)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(s)

server.listen(2)

con , addr = server.accept()

#con.send("hello word")
while True:
    send_date = raw_input(">> ")
    con.send(send_date)