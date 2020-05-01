ff = open("6c0c57fa88eb44f3b179a6e9798fc7b6","rb")
xx = ff.read()
ff.close()
print(xx)
mm=""
for i in xx:
	mm+=hex(i)[2:]
print(mm)

import hashlib
md5_val = hashlib.md5(xx).hexdigest()

print(md5_val)
import binascii
zz  = binascii.a2b_hex(md5_val)

ac=""
for i in range(len(zz)):
	ac+=chr(xx[i]^zz[i])
print(ac)
	