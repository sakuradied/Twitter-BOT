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

def F12(): #网页全屏化 本为F11
	win32api.keybd_event(122, 0, 0, 0)
	win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)

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
		print("图片编码格式解析失败")#异常处理
def qq():#将剪切板内容发送到QQ
	name = "DD术学家的#爱爱爱爱(指术力口)"  #要发送到的群名
	win32clipboard.OpenClipboard()
	win32clipboard.CloseClipboard()
	handle = win32gui.FindWindow(None, name)
	if True:
		win32gui.SendMessage(handle, 770, 0, 0)
		win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
def startweb(): #启动网页并调用截屏函数然后杀死Google浏览器进程
	webbrowser.open(str(web()))
	time.sleep(3)
	i=6
	F12() #模拟按键
	time.sleep(15)
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
	time.sleep(30)
	print("开始连接到",web())
	try:
		html = urllib.request.urlopen(str(web()),timeout=24).read()
		H_file = open(str(file_name()),"w")
		H_file.write(str(html))
		H_file.close()
	except Exception as e:
		print("ERROR:"+str(e))
		html_file()
def main():
	p= ["https://twitter.com/8_Prince","https://twitter.com/cosmobsp","https://twitter.com/Hiroaki_Arai_","https://twitter.com/NayutalieN","https://twitter.com/tomatowt","https://twitter.com/omu929","https://twitter.com/_Gom_","https://twitter.com/mikito_p_","https://twitter.com/scopscop","https://twitter.com/pinocchiop","https://twitter.com/neru_sleep","https://twitter.com/DECO27","https://twitter.com/40mP","https://twitter.com/uni_mafumafu","https://twitter.com/_MitchieM","https://twitter.com/doriko_","https://twitter.com/nashimotowe","https://twitter.com/tkomine","https://twitter.com/kz_lt","https://twitter.com/Omoi3965","https://twitter.com/Knoshin_nchaP","https://twitter.com/CCrusherP","https://twitter.com/hinataEW","https://twitter.com/vinegar_vinegar","https://twitter.com/iii0303_8","https://twitter.com/amehuruyoru49","https://twitter.com/amenomurakumo_p","https://twitter.com/yurryCanon","https://twitter.com/kemu8888","https://twitter.com/bass_ynk","https://twitter.com/696rkr","https://twitter.com/maretu01","https://twitter.com/samorira9","https://twitter.com/mothy_akuno","https://twitter.com/rerulili","https://twitter.com/tikandame","https://twitter.com/inabakumori","https://twitter.com/yasuhiro_vanq","https://twitter.com/Yuki_Jouet","https://twitter.com/balloon0120","https://twitter.com/WADATAKEAKI","https://twitter.com/harumaki_gohan","https://twitter.com/koyokoyokoyori","https://twitter.com/o0toa0o","https://twitter.com/wowaka","https://twitter.com/nabuna2","https://twitter.com/tghgworks_krsy","https://twitter.com/164203","https://twitter.com/sasakure__UK","https://twitter.com/siinamota","https://twitter.com/NishizawasanP","https://twitter.com/jin_jin_suruyo","https://twitter.com/buzz_g","https://twitter.com/GigaMozuku","https://twitter.com/MikanseiP","https://twitter.com/halyosy","https://twitter.com/asshole_wii","https://twitter.com/kairiki_bear","https://twitter.com/oO0Eve0Oo","https://twitter.com/_23ki_","https://twitter.com/xupxq_","https://twitter.com/nulut","https://twitter.com/tri_angl_e","https://twitter.com/wataru_sena","https://twitter.com/ryo_spcl"]		#这个数组中存放鸽子推特地址
	i=0
	n = [0]*99
	a = [0]*99
	while True:
		while i<= 64:
			with open('http.txt','w') as w:				#目前鸽子地址单独存放到http.txt文件
				w.write(p[i])
			w = os.path.isfile(str(file_name()))
			name=file_name()
			name=str(name)
			if w == True:
				html_file()
				file_size = stat(name)#读取文件大小 新文件 (
				file_size=file_size.st_size
				n[i] = file_size
				main = int(n[i]) - int(a[i])
				print("数据大小对比为:",main,"#这是第",i,"次循环")
				if main<2500:
					print(name,"这只鸽子没有发推检测下一只鸽子")
				else:
					a[i]=n[i]
					print("a=",a[i])
					print("鸽子",name,"发推了")
					startweb()
			else:
				html_file()
				file_size = stat(name)#读取文件大小 新文件 (
				file_size=file_size.st_size
				a[i] = file_size
				print("搜集的数据中")
			i=i+1
		i=0
main()
