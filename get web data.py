import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('http://data.pr4e.org/intro-short.txt', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
