'''
This module will deal with asynchronus execution 
'''
import threading,time



class timer:
	
	_thread=None # saving the current thread
	_alive = False # the state of the thread
	_call_number = None # the number of class for functions
	_repeat_count = None # the counter for the repetition
	_interval = None # the interval of sleeping
	_func = None #the timer function



	#constructor
	def __init__(self,func,interval=0,call_number=None):
		# initialisation
		self._func = func
		self._interval = interval
		self._call_number = call_number
	# the thread functions


	def thread_func(self):
		if(self._alive):
			if(self._call_number==None):
				while(self._alive):
					self.sleep_run()	
			else:
				self._repeat_count = self._call_number
				while(self._repeat_count >0):
					self.sleep_run()
					self._repeat_count -=1 

	# running the timer function after sleeping (the specified seconds)
	def sleep_run(self):
		time.sleep(self._interval)
		if(self._alive):
			self.get_func()() 

	# the function that make start the thread
	def start(self,asynchronus=True):	
		self._alive = True
		if(asynchronus):
			self._thread = threading.Thread(target=self.thread_func )
			self._thread.start()
		else:
			self.thread_func()

	def stop(self):
		self._alive = False
		if(self._thread != None):
			self._thread.join()

	def alive(self):
		return self._alive

	def repeat(self,call_number):
		self._call_number = call_number

	def get_count(self):
		return self._repeat_count

	def get_call_number(self):
		return self._call_number
	
	def get_interval(self):
		return self._interval

	def set_interval(self,inter):
		self._interval = inter
	def set_func(self,fct):
		self._func = fct
	def get_func(self):
		return self._func
