import sys
import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_address=('localhost',8000)


client_socket.connect(socket_address)
client_socket.send('GET /echo.php?message=helloworld HTTP/1.1\r\n\r\n') 
receive=client_socket.recv(1024)
client_socket.close()
print receive
