v39=[0x52,0x69,0x73,0x69,0x6e,0x67,0x5f,0x48,0x6f,0x70,0x70,0x65,0x72,0x21]
v1 = [17,8,6,10,15,20,42,59,47,3,47,4,16,72,62,0,7,16]
yy=""
for i in range(18):
	for j in range(0,257,1):
		if (~(j&v39[i%14]))&(j|v39[i%14]) ==v1[i]:
			yy+=chr(j)
			break
print(yy)
#Caucasus@s_ability

#abc文件是从源程序DUMP来的
ff = open("abc","rb")
red = ff.read()
ff.close()
#print(red)

y7=0x415

ff = open("result","wb")
for i in range(y7):
	mm = red[i] ^ord(yy[i%18])
	ff.write(bytes([mm]))
ff.close()

#然后把生成的result	文件扔给IDA，C转换代码，新建函数，F5

v78=19683
v79 = 0x8000000B
v26 = [0x1EA272,
0x206FC4,
0x1D2203,
0x1EEF55,
0x24F111,
0x193A7C,
0x1F3C38,
0x21566D,
0x2323BF,
0x2289F9,
0x1D2203,
0x21098A,
0x1E08AC,
0x223D16,
0x1F891B,
0x2370A2,
0x1E558F,
0x223D16,
0x1C883D,
0x1F891B,
0x2289F9,
0x1C883D,
0xEB773,
0xE6A90,
0xE6A90,
0xE6A90,
0xB1CCF,
0x1C883D,
2263545,
2283228,
2243862,
2184813,
2165130,
2027349,
1987983,
2243862,
1869885,
2283228,
2047032,
1909251,
2165130,
1869885,
2401326,
1987983,
2243862,
2184813,
885735,
2184813,
2165130,
1987983,
2460375,]
for i in range(0x33):
	for x in range(128):
		if (v78*x)%v79 == v26[i]:
			yy+=chr(x)
print(yy)