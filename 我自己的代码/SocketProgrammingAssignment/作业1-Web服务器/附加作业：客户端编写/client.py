import sys

from socket import *

serverName = '127.0.0.1'
serverPort = 8044
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

requestMessage = 'GET /1.html HTTP/1.1\r\n\r\n'
clientSocket.send(requestMessage.encode())
response = clientSocket.recv(1024).decode()
print(response)
