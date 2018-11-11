#We'll use date to name the file
import time as t
import webbrowser
import os
import subprocess
#path to double check file is not created so that script is called again, we won't overwrite
from os import path


#function passes a destination/string that is the folder location
def createFile():
	'''
	The script creates a text file at the passed in location and names file based on date
	'''
	#We want to prompt the user to enter the name of the file that he or she wants to create
	name = input ("Enter the name of the file that you want to create \n")
	#if file doesnt exist, then create the file
	if not(path.isfile(name)):
		#create file in a writable format
		f= open(name, 'w')
		#write new line 30 times
		f.write('\n'*30)
		f.close()
		input("done!!!")

def openFileAndWrite():
	name = input ("Enter the name of the file that you want to open \n")
	#The plus sign indicates that a new file will be created if there's none in existence
	webbrowser.open(name)

def openFileAndRead():
	name = input ("Enter the name of the file that you want to open \n")

	subprocess.call(['chmod', 'a-w', name])
	#The plus sign indicates that a new file will be created if there's none in existence
	webbrowser.open(name)

#if file name is equal to main or its main file that is being run, we will go ahead and call the function above
if __name__ == '__main__':
	option = int(input('''Select your option of choice:
		1. Create file
		2. Open file with write permission
		3. Open file with read only permission
		4. Open file and save written data
		5. View file attributes \n'''))

	if option == 1:
		createFile()

	elif option == 2:
		openFileAndWrite()

	elif option == 3:
		openFileAndRead()




