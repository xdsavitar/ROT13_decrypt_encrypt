import string
import random
import time
import sys
alphabet = list(string.ascii_lowercase)
encrypted = ""
decrypted = ""
print(alphabet)

def decrypt(text):
	global alphabet
	global decrypted



	for char in text:
		position_decrypt = (alphabet.index(f"{char}") + 1)
		new_position_decrypt = (position_decrypt - 13)

		if int(new_position_decrypt) < 0:
			new_position_alphabet = (26 - abs(new_position_decrypt))
			new_position_alphabet_n = alphabet[int(new_position_alphabet) - 1]
			decrypted += str(new_position_alphabet_n)

		elif int(new_position_decrypt > 0):
			new_position_alphabet_n = alphabet[int(new_position_decrypt) - 1]
			decrypted += new_position_alphabet_n

	print(decrypted)

 


def encrypt(text):
	global alphabet
	global encrypted

	for char in text:
		position_ = (alphabet.index(f"{char}") + 1)

		new_position = (position_ + 13)


		if new_position > 26:
			new_position = new_position - 26

			get_position = alphabet[int(new_position) - 1]

			encrypted += str(get_position)


		else:
			new_position = new_position

			get_position = alphabet[int(new_position) - 1]

			encrypted += str(get_position)




	print(f"Encryped Text {encrypted}")






def checkuserinput():
	operation = sys.argv[1]
	text = sys.argv[2]

	if str(operation) == "decrypt":
		decrypt(text)
	elif str(operation) == "encrypt":
		encrypt(text)



checkuserinput()