'''
ss = socket()          # 创建服务器套接字 
ss.bind()                # 套接字与地址绑定 
ss.listen()              # 监听连接 
inf_loop:               # 服务器无限循环     
	cs = ss.accept()        # 接受客户端连接     
	comm_loop:            # 通信循环         
		cs.recv()/cs.send()  # 对话（接收/发送）     
	cs.close()              # 关闭客户端套接字 
ss.close()               # 关闭服务器套接字#（可选） 
'''
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print("waiting for connection")
	tcpCliSock, addr = tcpSerSock.accept()
	print('....connected from :', addr)
	
	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send(bytes('[%s] %s', encoding="utf-8") % (bytes(ctime(), 'utf-8'), data))
		
	tcpCliSock.close()
tcpSerSock.close()