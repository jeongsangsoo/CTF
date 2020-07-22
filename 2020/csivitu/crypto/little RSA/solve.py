# -*- coding: cp936 -*-
import gmpy2
import time
from Crypto.Util.number import long_to_bytes
time.clock()
n = 64741
e = 42667
c = 32949
p = 101
q = 641

print ('[+]Found!')
print ('  [-]p =',p)
print ('  [-]q =',q)
print ('  [-]n =',p*q)
d = gmpy2.invert(e,(p-1)*(q-1))
print ('  [-]d =', d)
decoded = pow(c,d,n)
print('    raw_decoded is: ' + str(decoded))
print (b'  [-]m is:' + long_to_bytes(decoded))
print ('\n[!]Timer:', round(time.clock(),2), 's')
print ('[!]All Done!')