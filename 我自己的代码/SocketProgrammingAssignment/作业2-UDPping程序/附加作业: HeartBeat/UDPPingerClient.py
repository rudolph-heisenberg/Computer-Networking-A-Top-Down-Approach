# 命令行参数: 第一个是地址, 第二个是端口
import sys
from socket import *
from time import time

address = (sys.argv[1], int(sys.argv[2]))
clientSocket = socket(AF_INET, SOCK_DGRAM)

currentTime = time()
while True:
    if time() - currentTime < 5:
        continue
    message = 'Client is active... Time stamp: ' + str(time())
    clientSocket.sendto(message.encode(), address)
    currentTime = time()
