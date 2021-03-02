import onetimepad

p="hola"
cipher=onetimepad.encrypt(p,'random')
print "Cipher text is:"
print cipher
p=onetimepad.decrypt(cipher,'random')
print 'Plain text is:'
print p
print 'bye'
