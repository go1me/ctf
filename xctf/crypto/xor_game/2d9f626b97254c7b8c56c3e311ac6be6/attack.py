#!/usr/bin/env python 

import string

import collections

#import sets



# XORs two string

def strxor(a, b):     # xor two strings (trims the longer input)

    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])




import base64
ff = open("cipher.txt","rb")
xx =ff.read()
ff.close()
xx = base64.b64decode(xx).split("\n")
print(xx)

ciphers=[]
for i in xx:
	temp =""
	for j in i:
		temp+=hex(ord(j))[2:].rjust(2,"0")
	ciphers.append(temp)
print(ciphers)
print(len(ciphers))



#print(ciphers)
print(len(ciphers))

# The target ciphertext we want to crack

target_cipher = "07165300001c024d25500b651d310c79164906110400015300010b4744234b174352391b1c32491a1c0052131218050b1e526042160b522b01167f010b1517066f3c040c0047552f030c07177f051c310c020d4501"



# To store the final key

final_key = [None]*200

# To store the positions we know are broken

known_key_positions = set()



# For each ciphertext

for current_index, ciphertext in enumerate(ciphers):



	counter = collections.Counter()

	# for each other ciphertext

	for index, ciphertext2 in enumerate(ciphers):

		if current_index != index: # don't xor a ciphertext with itself
			#print("i "+ciphertext2)
			#print(ciphertext2.decode('hex'))

			for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): # Xor the two ciphertexts

				# If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)

				if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 # Increment the counter at this index

	knownSpaceIndexes = []



	# Loop through all positions where a space character was possible in the current_index cipher

	for ind, val in counter.items():

		# If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!

		if val >= 7: knownSpaceIndexes.append(ind)

	#print knownSpaceIndexes # Shows all the positions where we now know the key!



	# Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!

	xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)

	for index in knownSpaceIndexes:

		# Store the key's value at the correct position

		final_key[index] = xor_with_spaces[index].encode('hex')

		# Record that we known the key at this position

		known_key_positions.add(index)



# Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)

final_key_hex = ''.join([val if val is not None else '00' for val in final_key])

# Xor the currently known key with the target cipher

output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))

# Print the output, printing a * if that character is not known yet
print ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])



'''

Manual step

'''

# From the output this prints, we can manually complete the target plaintext from:

# The secuet-mes*age*is: Wh** usi|g **str*am cipher, nev***use th* k*y *ore than onc*

# to:

# The secret message is: When using a stream cipher, never use the key more than once



# We then confirm this is correct by producing the key from this, and decrpyting all the other messages to ensure they make grammatical sense

target_plaintext = "The secret message is: When using a stream cipher, never use the key more than once"

print target_plaintext

key = strxor(target_cipher.decode('hex'),target_plaintext)

for cipher in ciphers:

	print strxor(cipher.decode('hex'),key)