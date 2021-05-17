import socket

sock = socket.socket()

host = socket.gethostname()
sock.connect((host, 12345))
sock.setblocking(0)  # Now setting to non-blocking mode

data = "Hello Python\n" * 10 * 1024 * 1024  # Huge amount of data to be sent
assert sock.send(data)