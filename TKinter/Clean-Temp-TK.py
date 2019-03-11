# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window,0)
import tempfile
import os
import getpass
from Tkinter import *
import sys
import webbrowser
import subprocess
import threading
import tkMessageBox
from ctypes import *

cred = """\n\n
-----------------------------------------
  #  Desenvolvido por Adriel Freud!
  #  Contato: businessc0rp2k17@gmail.com 
  #  FB: http://www.facebook.com/xrn401
  #   =>DebutySecTeamSecurity<=
-----------------------------------------
\n"""
getuserprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
usr = getuserprof[1].strip('\r\n')
bar = "-:[ Limpador by Adriel ]:-"

temporario = tempfile.gettempdir()
root = Tk()
root.title(bar)

root['bg'] = 'black'
root.geometry("300x500+200+200")

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar)
menubar.add_cascade(label='Menu', menu=filemenu)
if windll.shell32.IsUserAnAdmin() == 0:
	tkMessageBox.showwarning("Warning", "Execute como administrador para uma limpeza Profunda!")
else:
	pass

def Creditos():
	tkMessageBox.showinfo("Creditos", cred)

filemenu.add_command(label='Creditos', command=Creditos)

def Open_channel():
	webbrowser.open('https://www.youtube.com/AdrielFreud')

filemenu.add_command(label='Canal', command=Open_channel)

def Github():
	webbrowser.open('https://github.com/AdrielFreud')

filemenu.add_command(label='Github', command=Github)

def Exit():
	sys.exit()
	exit()

filemenu.add_command(label='Exit', command=Exit)

def call_all_functions():
	list_thread = [clear_temp(), clear_prefetch(), clear_SoftwareDistribution(), clean_system(), cleanmgr()]
	for threads in list_thread:
		threading.Thread(target=threads, args=()).start()
	tkMessageBox.showinfo("Information", "Todos os arquivos inuteis foram retirados do seu computador, Obrigado por utilizar nosso programa! Att. AdrielFreud :)")

def clear_temp():
	try:
		os.chdir('C:\\Windows\\Temp')
		for temp1 in os.listdir('.'):
			if os.path.isdir(temp1) == True:
				os.system('rmdir %s /S /Q'%temp1)
			else:
				os.system('del %s /S /Q /F'%temp1)
		os.chdir('C:\\Temp')
		for temp2 in os.listdir('.'):
			if os.path.isdir(temp2) == True:
				os.system('rmdir %s /S /Q'%temp2)
			else:
				os.system('del %s /S /Q /F'%temp2)
		os.chdir(temporario)
		for temp3 in os.listdir('.'):
			if os.path.isdir(temp3) == True:
				os.system('rmdir %s /S /Q'%temp3)
			else:
				os.system('del %s /S /Q /F'%temp3)
	except:
		pass

def clear_prefetch():
	try:
		os.chdir('C:\\Windows\\Prefetch')
		for prefetch in os.listdir('.'):
			if os.path.isdir(prefetch) == True:
				os.system('rmdir %s /S /Q'%prefetch)
			else:
				os.system('del %s /S /Q /F'%prefetch)
	except:
		pass

def clear_SoftwareDistribution():
	try:
		os.chdir('C:\\Windows\\installer')
		for installer in os.listdir('.'):
			if os.path.isdir(installer) == True:
				os.system('rmdir %s /S /Q'%installer)
			else:
				os.system('del %s /S /Q /F'%installer)

		os.chdir('C:\\Windows\\SoftwareDistribution\\Download')
		for Software in os.listdir('.'):
			if os.path.isdir(Software) == True:
				os.system('rmdir %s /S /Q'%Software)
			else:
				os.system('del %s /S /Q /F'%Software)

		os.chdir('C:\\Windows\\Downloaded Program Files')
		for ProgramFiles in os.listdir('.'):
			if os.path.isdir(ProgramFiles) == True:
				os.system('rmdir %s /S /Q'%ProgramFiles)
			else:
				os.system('del %s /S /Q /F'%ProgramFiles)
				
	except:
		pass

info_sistema = Label(root, text='Limpador de Arquivos Temporarios do Sistema', bg='black', fg='white', font="Arial 10").place(x=12,y=10)
temp = Button(root, text='Clean TEMP', bg='#4F4F4F', fg='white', width=30, command=clear_temp).place(x=40, y=60)
prefetch = Button(root, text='Clean PREFETCH', bg='#4F4F4F', fg='white', width=30, command=clear_prefetch).place(x=40, y=100)
Distribution = Button(root, text='Clean SoftwareDistribution', bg='#4F4F4F', fg='white', width=30, command=clear_SoftwareDistribution).place(x=40, y=140)
####
info_clean_all = Label(root, text='> Limpador em Massa de Arquivos <', bg='black', fg='white', font="Arial 10").place(x=40, y=195)
clean_all = Button(root, text='Clean ALL FILES', bg='#4F4F4F', fg='white', width=30, command=call_all_functions).place(x=40, y=250)

# - Startup - #

def Add_Startup():
	tkMessageBox.showinfo('Information', '[!!] Adicionado ao Startup!')
	os.chdir('C:\\ProgramData')
	os.system('mkdir Startup-Cleandir')
	os.chdir('Startup-Cleandir/')
	with open('start.vbs', 'w') as w:
		w.write('Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "start.bat" & Chr(34), 0\nSet WshShell = Nothing')
		w.close()
		with open('clean.bat', 'w') as clean:
			clean.write('''
@echo off
cd "C:\\Windows\\SoftwareDistribution\\Download"
del * /S /Q /F
rmdir * /S /Q
cd "C:\\Windows\\Prefetch"
del * /S /Q /F
rmdir * /S /Q
cd "C:\\Windows\\Temp"
del * /S /Q /F
rmdir * /S /Q
cd "C:\\Temp"
del * /S /Q /F
rmdir * /S /Q
cd %temp%
del * /S /Q /F
rmdir * /S /Q''')
			clean.close()
			subprocess.Popen('reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "CleanDIRS" /d "%ProgramData%\\Startup-Cleandir\\start.vbs" /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

def Remove_Startup():
	tkMessageBox.showinfo('Information', '[!] Removendo Startup!')
	os.chdir('C:\\ProgramData')
	os.system('rmdir Startup-Cleandir /S /Q')
	print('\t[!] Startup Removido!\n')

def cleanmgr():
	tkMessageBox.showinfo('Information', "[@@@] Selecione todas as TextBox e Inicie uma Limpeza Profunda!")
	subprocess.Popen('RunDll32.exe inetcpl.cpl, ClearMyTracksByProcess 255', shell=True)
	subprocess.Popen('cleanmgr', shell=True).wait()

def clean_system():
	subprocess.Popen('ipconfig /flushdns', shell=True)
	os.chdir('%s\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE'%usr)

	for INetCache in os.listdir('.'):
		if os.path.isdir(INetCache) == True:
			os.system('rmdir %s /S /Q'%INetCache)
		else:
			os.system('del %s /S /Q /F'%INetCache)

	os.chdir('C:\\WINDOWS\\Offline Web Pages')	
	for Offline in os.listdir('.'):
		if os.path.isdir(Offline) == True:
			os.system('rmdir %s /S /Q'%Offline)
		else:
			os.system('del %s /S /Q /F'%Offline)

	os.chdir('C:\\Windows')
	try:
		os.system("del *.log /a /s /q /f")
	except:
		pass


Startup = Button(root, text='ADD Startup', bg='#4F4F4F', fg='white', width=30, command=Add_Startup).place(x=40, y=290)
remove_Startup = Button(root, text='REMOVE Startup', bg='#4F4F4F', fg='white', width=30, command=Remove_Startup).place(x=40, y=330)
Button(root, text='Limpeza de Disco', bg='#4F4F4F', fg='white', width=30, command=cleanmgr).place(x=40, y=370)
Button(root, text='Limpeza de Cache do Systema', bg='#4F4F4F', fg='white', width=30, command=clean_system).place(x=40, y=410)
Label(root, text='[ Agradeca ao Adriel Freud <3 ]', fg='white', bg='black', font="Arial 11").place(x=46, y=460)

root.mainloop()
