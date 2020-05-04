from socket import * 
serverPort = 65501
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('', serverPort)) 
print("The server is ready to receive")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) 
    modifiedMessage = message.decode().upper() 
    print("Server received "+message.decode()+" from "+str(clientAddress))
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)