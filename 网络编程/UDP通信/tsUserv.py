'''
ss = socket()                    # 创建服务器套接字 
ss.bind()                         # 绑定服务器套接字 
inf_loop:                         # 服务器无限循环     
cs = ss.recvfrom()/ss.sendto() # 关闭（接收/发送） 
ss.close()      # 关闭服务器套接字 
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21564
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print("waiting for message....")
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto(bytes('[%s] %s', encoding="utf-8") % (bytes(ctime(), 'utf-8'),data), addr)
	print("....received from and returned to:", addr)

udpSerSock.close()