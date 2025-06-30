import socket

# Server setup
s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))  # Bind to localhost on port 9999

# Listen for incoming connections
s.listen(3)
print("Waiting for connections...")

while True:
    c, addr = s.accept()

    print("Connected to", addr)

    c.send(bytes("Welcome", 'utf-8'))
    c.close()