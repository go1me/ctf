import base64
ff = open("cipher.txt","rb")
xx =ff.read()
ff.close()
xx = base64.b64decode(xx).split("\n")
#print(xx)

ciphers=[]
for i in xx:
	temp =""
	for j in i:
		temp+=hex(ord(j))[2:]
	ciphers.append(temp)
print(ciphers)