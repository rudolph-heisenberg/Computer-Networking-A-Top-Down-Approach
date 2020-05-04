from socket import * 
serverName = '127.0.0.1' 
serverPort = 65533
clientSocket = socket(AF_INET, SOCK_DGRAM) 
while True:
    message = input('Input lowercase sentence:') 
    clientSocket.sendto(message.encode(),(serverName, serverPort)) 
    print("Message sent: "+message+'\n')
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
    print("Message received: "+modifiedMessage.decode()) 
clientSocket.close()