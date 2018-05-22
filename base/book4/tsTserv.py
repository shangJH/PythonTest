'''
    TCP时间戳服务器
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21576
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from:", addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        # 这里send函数传输的是字节，需要进行转换
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data), encoding='utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
