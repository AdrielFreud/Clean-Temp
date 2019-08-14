import win32console, win32gui
con = 1
win32gui.ShowWindow(win32console.GetConsoleWindow() ,con)
import os, subprocess, shutil, webbrowser, platform
from tkinter import *
import tkinter.messagebox
from ctypes import *

if '64' in platform.machine():
	path = "x64"
else:
	path = "x86"

data = """****************************************************************
- Microsoft.NET Framework 3.5 Offline Installer 2.0
- AdrielFreud Laboratory 20011-2019
****************************************************************
- https://debutysec.wordpress.com
- Email: businessc0rp2k17@gmail.com
Click on "Start Installation" To Start Installation"""
ext = 'cmd /C dism /online /enable-feature /featurename:NetFX3 /source:"C:\\sources\\sxs" /LimitAccess'

def Troubleshooting():
	con = 1
	win32gui.ShowWindow(win32console.GetConsoleWindow(), con)
	os.system("cmd /C dism /online /cleanup-image /restorehealth")
	os.system(ext)

def about():
	webbrowser.open('https://pt.wikipedia.org/wiki/Microsoft_.NET')

def install_log():
	try:
		os.system('C:\\Windows\\logs\\DISM\\dism.log')
	except:
		pass

def disc_C():
	try:
		os.chdir('config\\%s'%path)
		shutil.move('sources', 'C:\\')
	except:
		pass

def disc_D():
	ext = ext.replace("C:\\", "D:\\")
	try:
		os.chdir('config\\%s'%path)
		shutil.move('sources', 'D:\\')
	except:
		pass

def disc_F():
	ext = ext.replace("C:\\", "F:\\")
	try:
		os.chdir('config\\%s'%path)
		shutil.move('sources', 'F:\\')
	except:
		pass
		
def disc_G():
	ext = ext.replace("C:\\", "G:\\")
	try:
		os.chdir('config\\%s'%path)
		shutil.move('sources', 'G:\\')
	except:
		pass

def main(root = Tk()):

	if windll.shell32.IsUserAnAdmin() == 0:
		tkinter.messagebox.showinfo("Microsoft .NET Reparir TOOL", "Please restart and run this application as administrator")

	root.title('Microsoft .NET Repair TOOL - Adriel Freud')
	root['bg'] = 'white'
	r1 = IntVar()

	Label(root, text="Microsoft .NET Framework", font="Arial 20", bg='white').place(x=5, y=5)
	Label(root, text="Powered Adriel Freud...", font="Arial 10", bg='white').place(x=15, y=40)

	Button(root, text="Open Install Log", command=install_log, font="Arial 10").place(x=490, y=25)
	Button(root, text="About App", command=about, font="Arial 10", width=12).place(x=490, y=60)
	
	Label(root, text="Installation Settings (Select Drive):", bg='white', font="Arial 11").place(x=20, y=100)
	Button(root, text="C:\\", bg='white', font='Arial 10', command=disc_C).place(x=40, y=140)
	Button(root, text="D:\\", bg='white', font='Arial 10', command=disc_D).place(x=80, y=140)
	Button(root, text="F:\\", bg='white', font='Arial 10', command=disc_F).place(x=120, y=140)
	Button(root, text="G:\\", bg='white', font='Arial 10', command=disc_G).place(x=160, y=140)

	Label(root, text="Information Console:", font="Arial 11", bg='white').place(x=10, y=230)
	texto = Text(root, height=8, width=75, bg="black", fg='white')
	texto.place(x=5, y=260)
	texto.insert(END, data)

	Button(root, text="Start Installation", font='Arial 10', command=Troubleshooting, height=2, width=15).place(x=450, y=200)

	root.geometry('600x400')
	root.mainloop()

main()
