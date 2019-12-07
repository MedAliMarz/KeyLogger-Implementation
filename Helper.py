'''
Helper Module contains shared functions related to Time handling
'''
import time
def now():
	return time.ctime()

def getDateString():
	# returns Date in the DD.mm.YYYY format
	local = time.localtime()
	result = f"{local.tm_mday}.{local.tm_mon}.{local.tm_year}"	
	return result	
def getTimeString(delimiter=':'):
	# returns time in the following format HH:MM:SS
	local = time.localtime()
	result = f"{local.tm_hour}{delimiter}{local.tm_min}{delimiter}{local.tm_sec}"
	return result

def getDateTimeString(delimiter=':'):
	return f"{getDateString()} {getTimeString(delimiter)}"
