import os
import codecs

path='original\\' #存放原代码
filename = os.listdir(path=path)
new = 'new\\' #新代码路径

for i in filename:
	file = codecs.open(path + i, 'r', 'utf-8').read().split('\n')
	mid = codecs.open(new + i, 'a', 'utf-8')
	for m in file:
		mid.write(m.strip('\r\n') + '  \n') #strip（）的括号里面填自己的博客的原换行符，不如我的是‘\r\n’,你的可能是‘\n’,可以使用notepad++查看你的是什么换行符
	
	mid.close()