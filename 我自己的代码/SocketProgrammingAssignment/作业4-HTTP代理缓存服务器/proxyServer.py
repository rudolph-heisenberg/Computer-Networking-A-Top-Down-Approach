# 备注
# 这个代理服务器, 实际上只能为一个网站提供代理缓存服务. 因为我把所有文件都存在根目录了. 
# 比如192.168.1.101:8000/1.html就存在了./1.html, 192.168.1.111:8000/b.html存在了./b.html
# 要实现对多个网站提供代理服务, 原理是一样的, 不影响.
# 我实现的代理服务器, 把404 NOT FOUND也存为了文件.
# 使用这个代理服务器通过局域网访问我自己写的server是可行的. 但是不知道为什么访问一般的http网页就会出问题.
# 我觉得可能是因为还有一些header里面的key-value pair没有写, 
# 对于真实在使用的服务器而言, 对于这种没有指明很多东西的请求, 服务器也许不知道怎么发送正确的回复
# 也有可能是真实使用的HTTP服务器比我想的复杂. 在我失败的尝试中, 我使用connect((网址, 80))这种连接方式. 
# 也许实际上要在一个投入使用的HTTP服务器里面访问东西, 不是这么操作的.
from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit()

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(('', int(sys.argv[1])))
tcpSerSock.listen(5)
# Fill in end.
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(2048).decode()  # Fill in start. # Fill in end.
    print(str(addr) + 'sent request message: '+message)
    # Extract the filename from the given message
    print('The file is: ' + message.split()[1])  # 这里打印出文件全称
    filename=message.split()[1].partition('/')[2]
    fileExist = "false"
    print('The filename is: ' + filename)
    try:
        # Check wether the file exist in the cache
        f = open(filename, "r")
        outputdata = f.read()
        fileExist = "true"  # 如果能进行到这步, 说明已经成功读入文件了.
        # ProxyServer finds a cache hit and generates a response message
        # Fill in start.
        tcpCliSock.send((outputdata).encode())
        # Fill in end.
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":  # 说明是读入文件出错, 也就是说没有这个文件
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)  # Fill in start. # Fill in end.
            hostn = (message.split()[1].partition('/')[0]).partition(':')[0]
            port = int((message.split()[1].partition('/')[0]).partition(':')[2])
            print('Host: ' + hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn,port))
                # Fill in end.
                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                requestMessage = "GET /" + filename + " HTTP/1.1\r\n"
                # Read the response into buffer
                # Fill in start.
                c.send(requestMessage.encode())
                message = c.recv(2048)
                tcpCliSock.send(message)
                # Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                # Fill in start.
                tmpFile.write(message)
            # Fill in end.
            except:
                print('Illegal request')
        else:  # 能到达这里, 说明不是文件读入出错了, 在32行之后再出错的.
            # HTTP response message for file not found
            # Fill in start.
            print('Error occurred during sending cached files')
        # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
# Fill in end.
