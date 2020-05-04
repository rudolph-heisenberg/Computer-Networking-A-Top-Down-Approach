from socket import *
serverPort = 35504
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print('The server is ready to receive.\n')
while True:
    print('Entering acception stage...')
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print('Received '+sentence.decode())
    capitalizedSentence = sentence.decode().upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
