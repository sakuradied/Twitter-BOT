import urllib.request
import os,time
from os import stat
import win32api
import win32con
import win32gui
from PIL import ImageGrab
import webbrowser
from ctypes import *
import win32clipboard

def zj():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
def fj():
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
def jiepin(): #将网页截屏为bmp图片文件
	time.sleep(3)
	im = ImageGrab.grab()
	time.sleep(3)
	im.save('img/fs.bmp')
def cp(): #将屏幕截图放入剪切板中
	aString=windll.user32.LoadImageW(0,"img/fs.bmp",win32con.IMAGE_BITMAP,0,0,win32con.LR_LOADFROMFILE)
	if aString !=0: 
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
		win32clipboard.CloseClipboard()
	else:
		print("图片编码格式解析失败")
def start():
	name = "DD术学家的"
	win32clipboard.OpenClipboard()
	win32clipboard.CloseClipboard()
	handle = win32gui.FindWindow(None, name)
	if True:
		win32gui.SendMessage(handle, 770, 0, 0)
		win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

def startweb(): #启动网页并调用截屏函数然后杀死Google浏览器进程
	webbrowser.open(str(web()))
	time.sleep(3)
	i=7
	time.sleep(20)
	while i>0:
		win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-100)
		i=i-1
	print("开始截屏")
	jiepin()
	time.sleep(2)
	os.system(r'taskkill /F /IM chrome.exe')
	cp()
	start()
	
def html_file():#获取网页内容
	print(web())
	response = urllib.request.urlopen(str(web()))
	html = response.read()
	H_file = open("8.html","w")
	H_file.write(str(html))
	H_file.close()
###############待修改############################
def rename():#文件名修改 new是旧文件 不是新文件 !!!! 
	w=os.path.isfile("new8.html")
	if w==True:
		html_file()
		contrast()
		os.remove("new8.html")
		os.rename("8.html","new8.html")
	else:
		os.rename("8.html","new8.html")
		rename()

def	contrast():#文件大小判断   同大小未更新  ( 检测点赞 以及转发对文件大小的影响 性 然后 使用  w1-w2 == 0 来判断 
	w1=stat(r"8.html")
	w1=w1.st_size
	w2=stat(r"new8.html")
	w2=w2.st_size
	a=w1-w2
	print(a)
	if a<700:
		print("未更新")
	else:
		print("检测到更新")
		startweb()
############################################################
def web():#读取文本内容来分辨是那个P主
	ini = open("http.txt")
	w=ini.readlines()
	return w[0]
	

def main():#将数组写文本来达到读取一个P主后读取另一个
	p=["https://twitter.com/8_Prince","https://twitter.com/QAQ_Y1"]
	i=0
	while i<=0:
		with open('http.txt','w') as w:
			w.write(p[i])
		i=i+1
		rename()

while True:
	main()
	time.sleep(60)

'''		
该文本为源测试文本 和部分思路 
def start(): #改为将文件存储到剪切板进行测试  https://blog.csdn.net/qq_34028920/article/details/79583587

	win32api.SetCursorPos([233,1058])
	zj()
	time.sleep(0.5)
	win32api.SetCursorPos([16,301])
	fj()
	time.sleep(0.3)
	win32api.SetCursorPos([80,361])
	zj()
	time.sleep(10)
	jiepin()
	time.sleep(0.3)
	win32api.SetCursorPos([405,1056])
	time.sleep(0.3)
	zj()
	time.sleep(0.3)
	win32api.SetCursorPos([254,250])
	time.sleep(0.3)
	fj()
	time.sleep(0.3)
	win32api.SetCursorPos([329,910])
	time.sleep(0.3)
	zj()
	time.sleep(0.3)
	win32api.SetCursorPos([563,1064])
	time.sleep(0.3)
	zj()
	time.sleep(0.3)
	win32api.SetCursorPos([1336,510])
	time.sleep(0.3)
	fj()
	time.sleep(0.2)
	win32api.SetCursorPos([1412,590])
	time.sleep(0.3)
	zj()
	time.sleep(0.5)
	win32api.SetCursorPos([1672,554])
	time.sleep(0.3)
	zj()
	
def main():
	while True:
		
		html_file()
		rename()
		time.sleep(600)
main()
	
'''
'''
		w=os.path.isfile("new8.html")
	if w==False:
		i=os.path.isfile("8.html")
		if i==True:
			os.rename("8.html","new8.html")
		else:
			html_file()
			os.rename("8.html","new8.html")
	else:
		os.remove("new8.html")
		rename()
''' 
