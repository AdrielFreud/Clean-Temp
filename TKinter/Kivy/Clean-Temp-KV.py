import tempfile, os, getpass, sys, webbrowser, subprocess, threading, kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.config import Config
from kivy.core.window import Window

Config.set("graphics", "width", "300")
Config.set("graphics", "height", "530")
Config.write()
menu = """\n\n
-----------------------------------------
  #  Desenvolvido por Adriel Freud!
  #  Contato: businessc0rp2k17@gmail.com 
  #  FB: http://www.facebook.com/xrn401
  #   =>DebutySecTeamSecurity<=
-----------------------------------------\n"""

getuserprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
usr = getuserprof[1].strip('\r\n')

def call_all_functions():
	list_thread = [clear_temp(), clear_prefetch(), clean_system(), cleanmgr(), clear_SoftwareDistribution()]
	for threads in list_thread:
		t = threading.Thread(target=threads, args=())
		t.start()

	for j in list_thread:
		j.join()

def clear_all():
	print(menu)
	try:
		call_all_functions()
		print("\n\t[+] Diretorios Limpados com sucesso!\n")
	except:
		print("\t[!!] Execute como Administrador!\n")

def clear_temp():
	print(menu)
	try:
		os.chdir('C:\\Windows\\Temp')
		for temp1 in os.listdir('.'):
			if os.path.isdir(temp1) == True:
				os.system('rmdir %s /S /Q'%temp1)
			else:
				os.system('del %s /S /Q /F'%temp1)
	except:
		print("\t[!!] Execute como Administrador!\n")
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
	except:
		print("\t[!!] Execute como Administrador!\n")

def clear_prefetch():
	print(menu)
	try:
		os.chdir('C:\\Windows\\Prefetch')
		for prefetch in os.listdir('.'):
			if os.path.isdir(prefetch) == True:
				os.system('rmdir %s /S /Q'%prefetch)
			else:
				os.system('del %s /S /Q /F'%prefetch)
	except:
		print("\t[!!] Execute como Administrador!\n")

def clear_SoftwareDistribution():
	print(menu)
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
		print("\t[!!] Execute como Administrador!\n")

def Add_Startup():
	print(menu)
	print('\t[!!] Adicionado ao Startup!\n')
	os.chdir('C:\\ProgramData')
	os.system('mkdir Startup-Cleandir')
	os.chdir('Startup-Cleandir')
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
rmdir * /S /Q''').strip('\n')
			clean.close()
			subprocess.Popen(r'reg add "HKCU\\SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Run" /v "CleanDIRS" /d "%ProgramData%\\Startup-Cleandir\\start.vbs" /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

def Remove_Startup():
	print(menu)
	print('\t[!] Removendo Startup!\n')
	os.chdir('C:\\ProgramData')
	os.system('rmdir Startup-Cleandir /S /Q')
	print('\t[!] Startup Removido!\n')

def cleanmgr():
	print(menu)
	print("\t[@@@] Selecione todas as TextBox e Inicie uma Limpeza Profunda!\n")
	proc = subprocess.Popen('cleanmgr', shell=True)
	proc.wait()

def clean_system():
	print("\t[!!!] Limpeza de Cache do Sistema!\n")

	subprocess.Popen('ipconfig /flushdns', shell=True)
 	subprocess.Popen('RunDll32.exe inetcpl.cpl , ClearMyTracksByProcess 255', shell=True)

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
	try:
		os.chdir('C:\\Windows')
		os.system("del *.log /a /s /q /f")
	except:
		pass

class Layout(FloatLayout):

	def __init__(self, **kwargs):
		super(Layout, self).__init__(**kwargs)
		Window.size = (300, 530)
		self.add_widget(Label(text='Limpador de Arquivos Temporarios do Sistema', font_size="13sp", pos=(0, 230)))
		temp = Button(text='Clean TEMP', width=250, height=30, font_size="13sp", pos=(22, 420))
		temp.size_hint = (None, None)
		temp.on_press = clear_temp

		prefetch = Button(text='Clean PREFETCH', width=250, height=30, font_size="13sp", pos=(22, 375))
		prefetch.size_hint = (None, None)
		prefetch.on_press = clear_prefetch

		Distribution = Button(text='Clean SoftwareDistribution', width=250, height=30, font_size="13sp", pos=(22, 330))
		Distribution.size_hint = (None, None)
		Distribution.on_press = clear_SoftwareDistribution

		self.add_widget(Label(text='> Limpador em Massa de Arquivos <', font_size="13sp", pos=(0, 35)))

		clean_all = Button(text='Clean ALL FILES', width=250, height=30, font_size="13sp", pos=(22, 240))
		clean_all.size_hint = (None, None)
		clean_all.on_press = clear_all

		Startup = Button(text='ADD Startup', width=250, height=30, font_size="13sp", pos=(22, 195))
		Startup.size_hint = (None, None)
		Startup.on_press = Add_Startup

		remove_Startup = Button(text='REMOVE Startup', width=250, height=30, font_size="13sp", pos=(22, 150))
		remove_Startup.size_hint = (None, None)
		remove_Startup.on_press = Remove_Startup

		Limpeza_disco = Button(text='Limpeza de Disco', width=250, height=30, font_size="13sp", pos=(22, 105))
		Limpeza_disco.size_hint = (None, None)
		Limpeza_disco.on_press = cleanmgr


		Limpeza_System = Button(text='Limpeza de Cache do Sistema', width=250, height=30, font_size="13sp", pos=(22, 60))
		Limpeza_System.size_hint = (None, None)
		Limpeza_System.on_press = clean_system

		self.add_widget(Label(text='[ Agradeca ao Adriel Freud <3 ]', font_size="13sp", pos=(0, -240)))

		self.add_widget(temp)
		self.add_widget(prefetch)
		self.add_widget(Distribution)
		self.add_widget(clean_all)
		self.add_widget(Startup)
		self.add_widget(remove_Startup)
		self.add_widget(Limpeza_disco)
		self.add_widget(Limpeza_System)

class MyApp(App):

	def build(self):
		self.title = "-:[Limpador by Adriel]:-"
		return Layout()

if __name__ == "__main__":
	MyApp().run()