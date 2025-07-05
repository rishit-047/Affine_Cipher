import math
import sys

def encrypt(text,a,b):
	encrypted_text=[]
	for char in text:
		if 32 <= ord(char) <= 126:
			num= char_num(char)
			encrypted_num = (a * num + b) % 95
			encrypted_char = num_char(encrypted_num)
			encrypted_text.append(encrypted_char)
		else:
			encrypted_text.append(char)
	return ''.join(encrypted_text)
	
# Coverting the result of ASCII chracter in between 0-94
def char_num(char):
	return ord(char) - 32

def num_char(num):
	return chr(num+32)

def valid_key_value(key):
	return 1<= key < 95 and math.gcd(key,95) == 1
	
def valid_shift_value(shift):
	return 0<= shift <= 95	

def read_Text(fileName):
	try:
		with open(fileName, 'r') as file:
			file_content = file.read()
		return file_content
	except FileNotFoundError:
		print(f"File {fileName} not found!!")
		sys.exit(1)
	except Exception as e:
		print(f"An error occurred while reading the file {e}")
		sys.exit(1) 

def write_Text(fileName, text):
	try:
		with open(fileName, 'w') as file:
			file.write(text)
		print(f"\nText has been successfully written to: {fileName}\n")
	except PermissionError:
		print(f"\nPermission Denied: Cannot write to {fileName}\n")
	except OSError as e:
		print(f"\nFilesystem error has occurred: {e}\n")
	except Exception as e:
		print(f"\nAn unexpectd error occurred: {e}\n")


if __name__ == "__main__":
	print("Welcome to the method of encrypting a message using Affine Cipher")
	print("""Choose an option:
1) Read the message from command prompt and write the encrypted nessage to a file
2) Read plaintext from an existing file, then print and save the encrypted text to a file.
3) Enter text manually via the command prompt, then save:
   - The plaintext in one file.
   - The encrypted text in a separate file.""")
	option = int(input("Choose from the above options: "))
	if option == 1:
		plaintext = input("\nEnter the plaintext: ")
		key_value = int(input("Enter the value of key: "))
		shift_value = int(input("Enter the shift value: "))
		if valid_key_value(key_value) and valid_shift_value(shift_value):
			print("\nProcess of the encrypting the message gas started. Please be patient....")
			encrypted_text = encrypt(plaintext, key_value, shift_value)
			print("Message has been successfully encrypted !!")
			fileName_encrpytedText = input("Enter the name of the file in which encrypted text has to be written: ")
			write_Text(fileName_encrpytedText, encrypted_text)
			print(f"\nFollowing is the value of key, shift and encrpted text:\nKey Value: {key_value}\nShift Value: {shift_value}\nEncrypted Text: {encrypted_text}")
		else:
			print("Invalid values has been provided\nExiting....")		
	
	elif option == 2:
   		fileName_plainText = input("Enter the name of the file: ")
   		plaintext = read_Text(fileName_plainText)
   		key_value = int(input("Enter the value of key: "))
   		shift_value = int(input("Enter the shift value: "))
   		if valid_key_value(key_value) and valid_shift_value(shift_value):
   			encrypted_text = encrypt(plaintext, key_value, shift_value)
   			fileName_encrpytedText = input("Enter the name of the file in which encrypted text has to be written: ")
   			write_Text(fileName_encrpytedText, encrypted_text)
   			print(f"\nFollowing is the value of key, shift and encrpted text:\nKey Value: {key_value}\nShift Value: {shift_value}\nEncrypted Text: {encrypted_text}")
   		else:
   			print("Invalid values has been provided\nExiting....")
	elif option == 3:
   		plaintext = input("Enter the text to be encrypted: ")
   		fileName_plainText = input("Enter the name of the file where plaintext has to be written: ")
   		write_Text(fileName_plainText, plaintext)
   		key_value = int(input("Enter the value of key: "))
   		shift_value = int(input("Enter the shift value: "))
   		if valid_key_value(key_value) and valid_shift_value(shift_value):
   			encrypted_text = encrypt(plaintext, key_value, shift_value)
   			fileName_encrpytedText = input("Enter the name of the file in which encrypted text has to be written: ")
   			write_Text(fileName_encrpytedText, encrypted_text)
   			print(f"\nFollowing is the value of key, shift and encrpted text:\nKey Value: {key_value}\nShift Value: {shift_value}\nEncrypted Text: {encrypted_text}")
   		else:
   			print("Invalid values has been provided\nExiting....")

