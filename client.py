import socket
c=socket.socket()
c.connect(('localhost',9999))
name =input('enter the name:')
print(c.recv(1024))
