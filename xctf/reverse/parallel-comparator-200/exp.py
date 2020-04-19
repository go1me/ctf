#这个数直接编译跑出来的
first_letter=108
print(first_letter)

differences = [0, 9, -9, -1, 13, -13, -4, -11, -9, -1, -7, 6, -13, 13, 3, 9, -13, -11, 6, -7]

mm =""
for i in range(len(differences)):
	mm+=chr(first_letter+differences[i]^0)
print(mm)