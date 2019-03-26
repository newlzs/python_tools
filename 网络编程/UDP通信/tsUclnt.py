'''
cs = socket()               # 创建客户端套接字 
comm_loop:                  # 通信循环     
	cs.sendto()/cs.recvfrom()   # 对话（发送/接收） 
cs.close()                   # 关闭客户端套接字 
'''

from socket import *

HOST = "localhost"
PORT = 21564
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = input("> ")
	data = bytes(data, encoding="utf-8")
	if not data:
		break
	udpCliSock.sendto(data, ADDR)
	data, ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print(data)
	
udpCliSock.close()