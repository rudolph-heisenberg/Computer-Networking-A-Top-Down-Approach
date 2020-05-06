import sys
from socket import *
if len(sys.argv) != 3:
    print('commandline arguments: addr and port')
    print('eg: python3 mailClient.py smtp.qq.com 25')
sys.exit()

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = (sys.argv[1], int(sys.argv[2]))
#Fill in start   #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO heisenberg\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# 登录邮箱
clientSocket.send('auth login\r\n'.encode())
print(clientSocket.recv(1024).decode())
clientSocket.send('base64 of your account\r\n'.encode())
print(clientSocket.recv(1024).decode())
clientSocket.send('base64 of your password\r\n'.encode())
print(clientSocket.recv(1024).decode())

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM: <sender email addr>\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = 'RCPT TO: <receipient email addr>\r\n'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send('DATA\r\n'.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
data = 'subject:A test mail\r\n' + 'FROM:<sender email addr>\r\n' + 'TO:<receipient email addr>\r\n' 
clientSocket.send(data.encode())
data = '\r\nHello, this is a mail sent using a simple SMTP client\r\n'
clientSocket.send(data.encode())
# Fill in end 

# Message ends with a single period.
# Fill in start
clientSocket.send('.\r\n'.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT\r\n'.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')
# Fill in end
 