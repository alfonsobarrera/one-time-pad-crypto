"""One Time Pad implemented by Alfonso Barrera Mora"""
from Crypto import Random
import sys

if len(sys.argv)<2:
	print "** HELP Provided: Syntax Error ** \nSyntax $: python oneTpad.py text-to-encrypt"
	quit() #Kills the program if less than 3 arguments.

else:
	plain=sys.argv[1] #Reading p=Plain Text
	plainarray=list(plain) # Converting Plan text into a char array.
	array=[]
	for i in plainarray:
		array.append(ord(i)) #Converting every char to its ascci/ordinaty representation (numeric).
	sumarray=[]
	randomVec=[]
	print "Plain in ascii: {}".format(array)
	print "Starting Encryption: C=pi+(ki mod 26)"
	for x,i in enumerate(array):
		k=int((Random.new().read(1)).encode("hex"),16) #Generate one key per char, k=Key
		randomVec.append(k) #Save a vector with all the keys/pad.
		sumarray.append(array[x]+k%26) #Star encrypting following C=p+(k mod 26) <== This is One time pad definition.


	print "Encryption Key:{}".format(randomVec) #This is the vector with all the keys.
	print "Cipher Text: {}".format(sumarray) #This is the Cipher text in decimal representation.
	print 'Starting Decryption: P: ci - (ki mod 26) '
	decarray=[] #Creating array to store decrytped values.
	for x,i in enumerate(sumarray):
		decarray.append(chr(sumarray[x]-(randomVec[x]%26))) #Proceed to Descrypt using P=c-(k mod 26), then convert to char.
	print "Decrypted Text: ", "".join(decarray) #print decrypted value.

