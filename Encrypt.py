'''
Encryption module (not really encryption)
Just base64 encoding mixed with few salts
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

def decode(toDecode):
	'''
	Base 64 encoding
	'''
	# the used alphabet
	alpha = r'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	# check padding
	removeBits=0
	if (toDecode.endswith('==')):
		removeBits= 4
		toDecode = toDecode[:-2]
	elif (toDecode.endswith('=')):
		removeBits = 2
		toDecode = toDecode[:-1] 
	
	# convert to binary format
	binaryFormat=""
	
	for c in toDecode:
		binaryFormat += bin(alpha.index(c))[2:].rjust(6,'0')
	
	if(removeBits):
		binaryFormat = binaryFormat[:-1*removeBits]
	
	result =""
	for i in range(round(len(binaryFormat)/8)):
		result += chr(int(binaryFormat[i*8:(i+1)*8],2))
	return result



def decrypt(msg):
	SALT1 = "$$="
	SALT2 = "w?w"
	SALT3 = "z#y"
	
	msg = msg.replace(SALT1,'').replace(SALT2,'').replace(SALT3,'')
	
	n1 = decode(msg)
	n2 = decode(n1[30:-12])
	n3 = decode(n2[6:-15])
	return n3

def encode(toEncode):
	'''
	Base 64 encoding
	'''
	# the used alphabet
	alpha = r'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	
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
		result += alpha[ int(binaryFormat[i*6:(i+1)*6], 2)]
	result+= padding

	return result


# uncomment to test the encrypt/decrypt methods
'''
test=["test1","AZ","test2AZASOHOSJ564084410454"]
for word in test:
	#print(encode(word),decode(encode(word)),decode(encode(word))==word)

	print(encrypt(word),decrypt(encrypt(word)),decrypt(encrypt(word))==word)
'''
