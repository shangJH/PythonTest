'''
   TCP时间戳客户端
'''

from socket import *

HOST = 'localhost'
PORT = 21576
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSocl = socket(AF_INET, SOCK_STREAM)
tcpCliSocl.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSocl.send(bytes(data, encoding="utf-8"))
    data = tcpCliSocl.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSocl.close()
