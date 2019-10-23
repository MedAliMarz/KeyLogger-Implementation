'''
Encryption module (not really encryption)
Just encoding in base64 with few salts
'''

def encrypt(toEncrypt):
	'''
	Encrypting using base64 encoding + salts
	Making the decoding harder
	'''
	SALT1 = "$$="
	SALT2 = "w?w"
	SALT3 = "z#y"
	n1 = encode(toEncrypt)
	n2 = encode( SALT3*2+ n1 + SALT1*5 )
	n3 = encode( SALT3*7 +SALT1*3 +  n2 + SALT2*4)

	return n3

def encode(toEncode):
	'''
	Base 64 encoding
	'''
	# the used alphabet
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	
	# check padding
	padding=""
	lastBits = len(toEncode) * 8 % 6
	if(lastBits == 4): padding = "="
	elif (lastBits ==2): padding = "=="

	# convert to binary format
	binaryFormat=""
	for c in toEncode:
		binaryFormat += bin(ord(c))[2:].rjust(8,'0')
	if(lastBits !=0): binaryFormat += '0' * (6-lastBits) 
	
	
	# convert to the base64 format and add padding
	result = ""
	for i in range(round(len(binaryFormat)/6)):
		result += alpha[ int(binaryFormat[i*5+i:(i+1)*6], 2)]
	result+= padding

	return result

