# 代码思路: 服务器超时时间是6秒
# 对于一个正常的客户端来说, 它每隔五秒发一次, 如果6秒server还没有收到第二个包, 说明这个包掉了
# 如果连续有6个包掉了, 就认为客户端已经挂掉了
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.settimeout(6)

# 接受第一个包
message, address = serverSocket.recvfrom(1024)
print(message.decode())
lastPacketTime = message.decode().split()[5]
lastPacketTime = float(lastPacketTime)

lastRecvPacketSeq = 0
loopCount = 0

while True:
	loopCount += 1
	if loopCount - lastRecvPacketSeq > 6:
		print('Client is down; server is shutting')
		break
	try:
		message, address = serverSocket.recvfrom(1024)
		print(message.decode())
		lastRecvPacketSeq = loopCount
	except timeout:
		print('A packet is lost...')

