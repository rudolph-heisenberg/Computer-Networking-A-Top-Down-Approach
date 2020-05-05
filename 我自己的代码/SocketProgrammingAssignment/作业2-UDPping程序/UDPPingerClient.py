# 命令行参数: 第一个是地址, 第二个是端口
import sys
import datetime
import threading
from socket import *
from time import time

address = (sys.argv[1], int(sys.argv[2]))
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
clientSocket.settimeout(1)  # recvfrom函数1秒没收到就视为超时了

for i in range(10):
    try:
        message = 'Ping ' + str(i) + ' ' + str(datetime.datetime.now())
        clientSocket.sendto(message.encode(), address)
        sendTime = time()
        message, addr = clientSocket.recvfrom(2048)
        recvTime = time()
        print(message.decode())
        print('RTT: ' + str((recvTime - sendTime) * 1000) + 'ms')  # 以毫秒显示RTT
    except timeout:
        print('Request timed out')
clientSocket.close()
