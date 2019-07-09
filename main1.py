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
import	re

def startqq():#截屏并发送到剪切板
	#截屏bmp图片文件
	time.sleep(3)
	im = ImageGrab.grab()
	time.sleep(3)
	im.save('img/fs.bmp')
	time.sleep(3)
	#将bmp图片文件保存到剪切板
	aString=windll.user32.LoadImageW(0,"img/fs.bmp",win32con.IMAGE_BITMAP,0,0,win32con.LR_LOADFROMFILE)
	if aString !=0: 
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
		win32clipboard.CloseClipboard()
	else:
		print("图片编码格式解析失败")

def qq():#将剪切板内容发送到QQ
	name = "EXECUTION"  #要发送到的群名
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
	startqq()
	time.sleep(2)
	os.system(r'taskkill /F /IM chrome.exe')
	
	qq()
def web():#读取文本内容来分辨是那个P主
	ini = open("http.txt")
	w=ini.readlines()
	return w[0]
	
def file_name(): #读取鸽子名
	name = open("http.txt")
	w=name.read()
	name.close()
	w=re.findall(r"com/(.+)",w)
	w=w[0]
	return w

def html_file():#获取网页内容  并保存到鸽子的文件中
	print("开始连接到",web())
	response = urllib.request.urlopen(str(web()),timeout=24)
	html = response.read()
	H_file = open(str(file_name()),"w")
	H_file.write(str(html))
	H_file.close()

	
def file_size():
	id_file = open("id.txt")
	i = id_file.read()
	id_file.close()
	i = i[0]
	i=int(i)
	w=[0]*10
	a=[0]*10
	name=file_name()
	name=str(name)
	file_size = stat(name)#读取文件大小 新文件 (
	file_size=file_size.st_size
	print("当前文件大小",file_size,"0")
	file_size=int(file_size)
	w[i] = file_size
	time.sleep(20)
	html_file()
	file_size = stat(name)
	file_size=file_size.st_size #读取文件大小 新文件 X2(
	file_size=int(file_size)
	print("当前文件大小",file_size,"1")
	a[i] = file_size
	pd = a[i]-w[i]
	
	if pd>700:
		print("鸽子",file_name(),"发推了")
		startweb()
	else:
		print(file_name(),"这只鸽子没有发推检测下一只鸽子")
def config():
	p=["https://twitter.com/8_Prince","https://twitter.com/cosmobsp","https://twitter.com/cosmobsp","https://twitter.com/Hiroaki_Arai_","https://twitter.com/NayutalieN"]			#这个数组中存放鸽子推特地址
	i=0
	while i<=4:
		with open('http.txt','w') as w:				#目前鸽子地址单独存放到http.txt文件
			w.write(p[i])
		with open('id.txt','w') as id:				#以像文本存放数字的形式来判断数组位置
			id.write(str(i))
		i=i+1
		html_file()
		file_size()
while True:
	
	config()
