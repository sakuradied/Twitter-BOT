# -*- coding: utf-8 -*-
from urllib import request,error,parse
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
import random
import http.client
import hashlib

def Twitter_img():
	im = ImageGrab.grab()
	im.save('save.bmp')

def Twitter_img_save():
	aString=windll.user32.LoadImageW(0,"save.bmp",win32con.IMAGE_BITMAP,0,0,win32con.LR_LOADFROMFILE)	#解析图片到剪切板
	if aString !=0: 
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
		win32clipboard.CloseClipboard()
	else:
		print("图片编码格式解析失败")
	# 将消息写到剪贴板
def F11():
	win32api.keybd_event(122, 0, 0, 0)
	win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)
	
def web_start(Turl):
	webbrowser.open(str(Turl))
	time.sleep(20)
	F11()
	time.sleep(1)
	Twitter_img()
	os.system(r'taskkill /F /IM chrome.exe')

def Send_img(QQ_group_name):
	# 获取qq窗口句柄
	qq1 = win32gui.FindWindow(None, QQ_group_name)
	# 投递剪贴板消息到QQ窗体
	win32gui.SendMessage(qq1, 258, 22, 2080193)
	win32gui.SendMessage(qq1, 770, 0, 0)
    # 模拟按下回车键
	win32gui.SendMessage(qq1, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
	win32gui.SendMessage(qq1, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
	print("尝试发送")


def fanyi(text):	#调用百度的API 
	appid = '20190824000329276'	#APP ID
	secretKey = 'AzHQHfKcphYrueq8XiO3'	#秘钥
	httpClient = None
	myurl = '/api/trans/vip/translate'
	q = text
	fromLang = 'auto'
	toLang = 'zh'
	salt = random.randint(32768, 65536)
	sign = appid+q+str(salt)+secretKey
	m1 = hashlib.md5()
	m1.update(sign.encode(encoding='utf-8'))
	sign = m1.hexdigest()
	myurl = myurl+'?appid='+appid+'&q='+parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign 
	try:
		httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
		httpClient.request('GET', myurl)
		response = httpClient.getresponse()
		w = response.read().decode('utf-8')
		w = eval(w)
		for line in w['trans_result']:
			return(line['dst'])
	except Exception as e:
		print(e)
	finally:
		if httpClient:
			httpClient.close()


def setText(aString):
    '''设置剪贴板文本'''
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    win32clipboard.CloseClipboard()

def qqbot(QQ_group_name,date_qq):
	# 将消息写到剪贴板
	setText(date_qq)
	# 获取qq窗口句柄
	qq = win32gui.FindWindow(None, QQ_group_name)
	# 投递剪贴板消息到QQ窗体
	win32gui.SendMessage(qq, 258, 22, 2080193)
	win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
	win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
	win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
	print("尝试发送")
def get_QQ_group_name():
	w=open('qqgroup.ini')
	QQgroup_name=w.readlines()
	QQgroup_name=QQgroup_name[0]
	w.close()
	print('刷新群名称中,获取到的群名称为:',QQgroup_name)
	return(QQgroup_name)
	
def file_name(i): #读取鸽子名
	ifcong=open("config.ini")	#读取配置文件依次获取地址
	url=ifcong.readlines()
	url=url[i]
	url=re.findall(r"com/(.+)",str(url)) #利用正则过滤出鸽子名(Twitter后缀)
	url=url[0]
	return url
	
def count():#统计共有多少位鸽子
	count=open("config.ini")
	count_o=count.readlines()
	count.close()
	count_o=re.findall(r'twitter(\S.)',str(count_o))
	i=len(count_o)
	return(i)

def date_id(ii):
	ifcong=open("config.ini")	#读取配置文件依次获取地址
	url=ifcong.readlines()		# 
	url=url[ii]					#读取指定行数
	print("获取当前地址为:",url)	#
	head = {
		'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML,  like Gecko) Chrome/18.0.1025.166  Safari/535.19'
	}
	#head['Accept-Language:'] = 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
	req = request.Request(url, headers=head)
	#传入创建好的Request对象
	print("-----读取鸽子:",file_name(ii),"中-----")
	while True:
		try:
			response = request.urlopen(req,timeout=12)	
			break
		except error.URLError as e:
			print(e.reason)
	html = response.read().decode('utf-8')
	#print(html)
	date_id = re.search(r'name="tweet_(\d*)', str(html))
	date_id=date_id[1]
	return(date_id)#返回连接后缀
	
def date_Twitter(ii): #检测到更新并获取更新的文字内容
	head = {
		'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML,  like Gecko) Chrome/18.0.1025.166  Safari/535.19'
	}
	date_url="https://twitter.com/"+file_name(ii)+"/status/"+date_id(ii)
	#print("最新推特地址为:",date_url)
	date_Twitter = request.Request(date_url, headers=head)
	print("等待获取网页文字中")
	while True:
		try:
			response = request.urlopen(date_Twitter,timeout=12)
			break
		except error.URLError as e:
			print(e.reason)
	twitter_html = response.read().decode('utf-8')
	date_wb = re.search(r'class="dir-ltr" dir="ltr">(.*)<a href=', str(twitter_html))	#利用正则过滤图片 如果没有图片则再次过滤无用标签
	if	date_wb == None:
		date_wb = re.search(r'class="dir-ltr" dir="ltr">(.*)', str(twitter_html))
		#过滤链接格式 如果检测到链接  则提取所有的文字  再次过滤 出链接  可以使用  re.findall 
	return(date_wb[1])

def main():
	jiuID = [0] * 99
	newID = [0] * 99

	while True:
		count_i=count()
		
		print("刷新鸽子数量: 共有鸽子",count_i,"只")
		i=0
		while i < count_i:
			#print("获取数字地址:",date_id(i))
			newID[i] = date_id(i)
			print("1:旧",jiuID[i])
			print("1:新",newID[i])
			if jiuID[i] == 0:
				jiuID[i] = newID[i]
				print("2:旧",jiuID[i])
				print("2:新",newID[i])
				print("等待刷新数据中")
			else:
				if jiuID[i] == newID[i]:
					print(file_name(i),":未更新")
				else:
					jiuID[i]=newID[i]
					wb=date_Twitter(i) #获取指定鸽子文本内容
					TTurl="https://twitter.com/"+file_name(i)+"/status/"+date_id(i)
					web_start(TTurl)
					date_q=file_name(i)+"发推啦:\n原文为:\n"+wb+"\n机翻:\n "+fanyi(wb)+"\nURL:"+TTurl
					print(date_q)
					qqbot(get_QQ_group_name(),date_q)
					Twitter_img_save()
					Send_img(get_QQ_group_name())
			i=i+1
main()