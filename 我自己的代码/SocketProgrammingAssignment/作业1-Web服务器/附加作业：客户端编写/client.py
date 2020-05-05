import sys

from socket import *

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

requestMessage = 'GET /'+ sys.argv[3] +' HTTP/1.1\r\n\r\n'
clientSocket.send(requestMessage.encode())
response = clientSocket.recv(1024).decode()
storeFile = open('storeFile.txt',mode='w')
storeFile.write(response)
