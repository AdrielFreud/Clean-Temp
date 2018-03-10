# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

menu = """\n\n
-----------------------------------------

  #  Desenvolvido por Adriel Freud!
  #  Contato: businessc0rp2k17@gmail.com 
  #  FB: http://www.facebook.com/xrn401
  #   =>DebutySecTeamSecurity<=

-----------------------------------------
\n"""

import tempfile
import os
import getpass
from Tkinter import *
import sys
import webbrowser
import subprocess
import threading

os.system('color a')
print(menu)

temporario = tempfile.gettempdir()
root = Tk()
root.title('--=> Limpador by Adriel Freud <=--')

root['bg'] = 'black'
root.geometry("300x500+200+200")

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar)
menubar.add_cascade(label='Menu', menu=filemenu)

def Creditos():
	os.system('color a')
	print(menu)

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
	list_thread = [clear_temp(), clear_prefetch(), clean_system(), cleanmgr(), clear_SoftwareDistribution()]
	for threads in list_thread:
		t = threading.Thread(target=threads, args=())
		t.start()

	for j in list_thread:
		j.join()

def clear_all():
	print(menu)
	print("\n\t[!] Limpando todos os arquivos temporarios!\n")
	try:
		call_all_functions()
		print("\n\t[+] Diretorios Limpados com sucesso!\n\n")
	except:
		print("\n\n\t[!!] Execute como Administrador!\n\n")

def clear_temp():
	print(menu)
	try:
		print("\t[!!!] Limpando TEMP!\n\n")

		os.chdir('C:\\Windows\\Temp')
		for temp1 in os.listdir('.'):
			if os.path.isdir(temp1) == True:
				os.system('rmdir %s /S /Q'%temp1)
			else:
				os.system('del %s /S /Q /F'%temp1)
	except:
		print("\n\n\t[!!] Execute como Administrador!\n\n")
	try:
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

		print("\t[+++] Arquivos Limpados!\n\n")
	except:
		print("\n\n\t[!!] Execute como Administrador!\n\n")

def clear_prefetch():
	print(menu)
	print("\t[!!!] Limpando PREFETCH!\n")
	try:
		os.chdir('C:\\Windows\\Prefetch')
		for prefetch in os.listdir('.'):
			if os.path.isdir(prefetch) == True:
				os.system('rmdir %s /S /Q'%prefetch)
			else:
				os.system('del %s /S /Q /F'%prefetch)
		print("\n\t[+++] Prefetch Limpada!\n\n")
	except:
		print("\n\n\t[!!] Execute como Administrador!\n\n")

def clear_SoftwareDistribution():
	print(menu)
	print("\t[!!!] Limpando SoftwareDistribution!\n\n")
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
				
		print("\n\t[+++] Limpada!\n\n")
	except:
		print("\n\n\t[!!] Execute como Administrador!\n\n")


info_sistema = Label(root, text='>Limpador de Arquivos Temporarios do Sistema<', bg='black', fg='green').place(x=10,y=10)
temp = Button(root, text='Clean TEMP', bg='black', fg='green', width=30, command=clear_temp).place(x=35, y=50)
prefetch = Button(root, text='Clean PREFETCH', bg='black', fg='green', width=30, command=clear_prefetch).place(x=35, y=90)
Distribution = Button(root, text='Clean SoftwareDistribution', bg='black', fg='green', width=30, command=clear_SoftwareDistribution).place(x=35, y=130)
####
info_clean_all = Label(root, text='Limpar Todos os Arquivos Temporarios?', bg='black', fg='green').place(x=35,y=190)
clean_all = Button(root, text='Clean ALL FILES', bg='black', fg='green', width=30, command=clear_all).place(x=35, y=240)

# - Startup - #

def Add_Startup():
	print(menu)
	print('\n\t[!!] Adicionado ao Startup!\n\n')
	os.chdir('C:\\programdata')
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
			subprocess.Popen(r'reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "CleanDIRS" /d "%ProgramData%\Startup-Cleandir\start.vbs" /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

def Remove_Startup():
	print(menu)
	print('\n\t[!] Removendo Startup!\n\n')
	os.chdir('C:\\ProgramData')
	os.system('rmdir Startup-Cleandir /S /Q')
	print('\n\t[!] Startup Removido!\n\n')

def cleanmgr():
	print(menu)
	print("\n\n\t[@@@] Selecione todas as TextBox e Inicie uma Limpeza Profunda!\n\n")
	proc = subprocess.Popen('cleanmgr', shell=True)
	proc.wait()

def clean_system():
	print("\n\n\t[!!!] Limpeza de Cache do Sistema!\n\n")

	subprocess.Popen('ipconfig /flushdns', shell=True)
 	subprocess.Popen('RunDll32.exe inetcpl.cpl , ClearMyTracksByProcess 255', shell=True)

	os.chdir('C:\\Users\\adrie_000\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE')
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

Startup = Button(root, text='ADD Startup', bg='black', fg='green', width=30, command=Add_Startup).place(x=35, y=280)
remove_Startup = Button(root, text='REMOVE Startup', bg='black', fg='green', width=30, command=Remove_Startup).place(x=35, y=320)
Button(root, text='Limpeza de Disco', bg='black', fg='green', width=30, command=cleanmgr).place(x=35, y=360)
Button(root, text='Limpeza de Cache do Systema', bg='black', fg='green', width=30, command=clean_system).place(x=35, y=400)
Label(root, text='Agradeca ao Adriel Freud, hahaha :) <3', fg='green', bg='black').place(x=35, y=470)

root.mainloop()