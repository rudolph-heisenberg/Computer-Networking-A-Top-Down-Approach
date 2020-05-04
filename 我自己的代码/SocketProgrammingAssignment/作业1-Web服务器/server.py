#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
#Fill in start 
serverPort = 8041
serverSocket.bind(('',serverPort))
with open('visitorCount.txt') as file_count:
    countStr=file_count.readlines()
    count=int(countStr[0].rstrip())
#Fill in end 
while True:  
    serverSocket.listen(1)   
    #Establish the connection    
    print('Ready to serve...')     
    connectionSocket, addr =  serverSocket.accept()
    count=count+1
    ff=open('visitorCount.txt',mode='w')
    ff.write(str(count))
    try:         
        message = connectionSocket.recv(1234)#Fill in start    #Fill in end
        filename = message.split()[1]                          
        f = open(filename[1:])
        outputdata = f.read() #Fill in start  # Fill in end
        #Send one HTTP header line into socket         
        #Fill in start
        header='HTTP/1.1 200 OK\r\nServer: Local Machine\r\n\r\n'
        #outputdata 
        connectionSocket.send(header.encode())        
        #Fill in end    

        #Send the content of the requested file to the client
        outputdata+='\n<p>您是本站的第'+str(count)+'位访客</p>\n</body>\n</html>\n'
        connectionSocket.send(outputdata.encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        notfound='HTTP/1.1 404 Not Found\r\nServer: Local Machine\r\n\r\n'
        connectionSocket.send(notfound.encode())
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end             
serverSocket.close()