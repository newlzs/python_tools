'''
cs = socket()               # 创建客户端套接字 
cs.connect()                # 尝试连接服务器 
comm_loop:                  # 通信循环     
	cs.send()/cs.recv()     # 对话（发送/接收） 
cs.close()                  # 关闭客户端套接字
'''

from socket import *

HOST = 'localhost'
#HOST = "172.31.61.41"
PORT = 21567
BURSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = input('> ')
	data = bytes(data, encoding='utf-8')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BURSIZ)
	if not data:
		break
	print(data.decode('utf-8'))
	
tcpCliSock.close()