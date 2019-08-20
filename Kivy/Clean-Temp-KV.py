# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

import win32gui, win32con
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
import tempfile
import os
import getpass
import sys
import webbrowser
import subprocess
import threading
from ctypes import *
from tkinter import messagebox
from tkinter import Tk

import kivy
kivy.require('1.9.1')
import kivy.uix.popup
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

getuserprof = subprocess.check_output("set USERPROFILE", shell=True).split(b'=')
usr = getuserprof[1].strip(b"\r\n")
root = Tk()
root.withdraw()

if windll.shell32.IsUserAnAdmin() == 0:
	messagebox.showwarning("Warning", "Execute como administrador para uma limpeza Profunda!")
else:
	pass

def Creditos():
	tkMessageBox.showinfo("Creditos", cred)

def call_all_functions():
	list_thread = [clear_temp(), clear_prefetch(), clear_SoftwareDistribution(), clean_system(), cleanmgr()]
	for threads in list_thread:
		threading.Thread(target=threads, args=()).start()
	messagebox.showwarning("Warning", "Todos os arquivos inuteis foram retirados do seu computador, Obrigado por utilizar nosso programa! Att. AdrielFreud :)")
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

def Add_Startup():
	messagebox.showwarning('Information', '[!!] Adicionado ao Startup!')
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
	messagebox.showwarning('Information', '[!] Removendo Startup!')
	os.chdir('C:\\ProgramData')
	os.system('rmdir Startup-Cleandir /S /Q')
	print('\t[!] Startup Removido!\n')

def cleanmgr():
	messagebox.showwarning('Information', "[@@@] Selecione todas as TextBox e Inicie uma Limpeza Profunda!")
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
		clean_all.on_press = call_all_functions

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