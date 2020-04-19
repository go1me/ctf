import math
v3 = ["Dufhbmf","pG`imos","ewUglpt"]
a=""
for i in range(12):
	xx = 2*int(i/3)
	print(xx)
	a+= chr(ord(v3[i%3][xx])-1)
print(a)