from socket import *
serverName = '127.0.0.1'
serverPort = 35501  
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Please input the message to be modified by the server: ')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024).decode()
    print('The modified sentence received from the server is: '+modifiedSentence+'\n')
