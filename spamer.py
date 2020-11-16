import pyautogui
import time
import os

os.system('clear')
print ("""
	\033[32;1m		                     _                   
	\033[32;1m ___ _ __   __ _ _ __ ___ (_)_ __   __ _       
	\033[32;1m/ __| '_ \ / _` | '_ ` _ \| | '_ \ / _` |      
	\033[32;1m\__ \ |_) | (_| | | | | | | | | | | (_| |_ _ _ 
	\033[32;1m|___/ .__/ \__,_|_| |_| |_|_|_| |_|\__, (_|_|_)
	\033[32;1m    |_|                            |___/ 

	by: ALWAYS-Ch3K--

	\033[0m""")
time.sleep(2)
info =('\033[33;1mgo out form terminal and aplication anything\033[0m')
print(info.center(106,'='))
info2 =('\033[33;1mbecause the programs has been runing\033[0m')
print(info2.center(106,'='))
input ('\033[36;1mpress ENTER:\033[0m')
print  ('\033[36;1mto continue, pelase insert----->> \033[0m')

msg = input("Enter the message: ")
n = input("how many to spams ?: ")

print("\033[33;1m1 spams = 10 spams\033[0m")
geting = ("\033[33;1mgo out of your console and see in your target:)---->>\033[0m")
print(geting.center(106,'+'))

print ('\033[0;32m3\033[0m')
time.sleep(2)
print ('\033[0;32m2\033[0')
time.sleep(2)
print ('\033[0;32m1\033[0m')
time.sleep(3)

os.system('clear')

count = 10
while(count != 0):
	print(count)
	#time.sleep(1)
	count -= 1

	print("\033[0;32mspaming...\033[0m")

	for i in range(0,int(n)):
		pyautogui.typewrite(msg + '\n')

		end =('\033[0;32mspaming sucessfully')
		print(end.center(106,'-'))
