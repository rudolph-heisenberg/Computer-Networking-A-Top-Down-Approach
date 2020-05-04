import pdb
from socket import *
from threading import Thread


def init():
    global serverSocket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 8044
    serverSocket.bind(('', serverPort))
    with open('visitorCount.txt') as file_count:
        countStr = file_count.read()
        global count
        count = int(countStr)
    serverSocket.listen(5)
    print('Server is listening...')


def requestHandler(currentSocket):
    try:
        message = currentSocket.recv(2048)
        filename = message.split()[1]
        file_to_handle = open(filename[1:])
        responseData = file_to_handle.read()
        header = 'HTTP/1.1 200 OK\r\nServer: Local Machine\r\n\r\n'
        global count
        count = count + 1
        file_to_handle = open('visitorCount.txt', mode='w')
        file_to_handle.write(str(count))
        responseData += '\n<p>您是本站的第' + str(count) + '位访客</p>\n</body>\n</html>\n'
        currentSocket.send((header+responseData).encode())
        currentSocket.close()
    except IOError:
        notfound = 'HTTP/1.1 404 Not Found\r\nServer: Local Machine\r\n\r\n'
        connectionSocket.send(notfound.encode())
        connectionSocket.close()
    # threadPool.remove(connectionSocket)


# threadPool=[]
global count
count = 0
init()
while True:
    connectionSocket, addr = serverSocket.accept()
    # threadPool.append(connectionSocket)
    thread = Thread(target=requestHandler, args=(connectionSocket,))
    thread.setDaemon(True)
    thread.start()
