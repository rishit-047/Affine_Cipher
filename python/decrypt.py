import math
import sys 

def decrypt(ciphertext,a,b):
	inverse = pow(a,-1,95)
	decrypted=[]
	for char in ciphertext:
		if 32 <= ord(char) <= 126:
			num = char_num(char)
			decrypted_num = (inverse * (num - b ) ) % 95
			decrypted_char = num_char(decrypted_num)
			decrypted.append(decrypted_char)
		else:
			decrypted.append(decrypted_char)
			
	return ''.join(decrypted)
			
	
	
# Coverting the result of ASCII chracter in between 0-94
def char_num(char):
        return ord(char) - 32

def num_char(num):
        return chr(num+32)

def valid_key_value(key):
        return 1 <= key < 95 and math.gcd(key,95) == 1

def valid_shift_value(shift):
        return 0 <= shift <= 95
        
def read_Text(fileName):
	try:
		with open(fileName,'r') as file:
			file_content = file.read()
		return file_content
	except FileNotFoundError:
		print(f"File {fileName} could not be found !!")
		sys.exit(1)
	except Exception as e:
		print(f"An unexpected error has occurred: {e}")
		sys.exit(1)
def write_Text(fileName,text):
	try:
		with open (fileName, 'w') as file:
			file.write(text)
		print(f"\nText has been successfully writtent to: {fileName}")
	except PermissionError:
		print(f"Permission Denied: Cannot write to {fileName}")
		sys.exit(1)
	except OSError as e:
		print(f"Filesystem error has occuerred: {e}")
		sys.exit(1)
	except Exception as e:
		print(f"An unexpected error has occurred: {e}")	
		sys.exit(1)


if __name__ == "__main__":
        print("Welcome to the method of decrypting a message using Affine Cipher")
        print("""Choose an option:
1) Read the encrypted message from command prompt and write to a file
2) Read the encrypted message from a file and write to another file""")
        option = int(input("\nChoose from the above options: "))
        if option == 1:
        	encrypted_text = input("Enter the encrypted text: ")
        	key_value = int(input("Enter the value of key: "))
        	shift_value = int(input("Enter the shift value: "))
        	if valid_key_value(key_value) and valid_shift_value(shift_value):
        		print("\nProcess of decrypting the message has started. Please be patient....")
        		decrypted_text = decrypt(encrypted_text, key_value, shift_value)
        		print("Message has been successfully decrypted !!")
        		fileName_decrpytedText = input("Enter the name of the file in which decrypted text has to be written: ")
        		write_Text(fileName_decrpytedText, decrypted_text)
        		print(f"\nFollowing is the value of key, shift and decrpted text:\nKey Value: {key_value}\nShift Value: {shift_value}\nDecrypted Text: {decrypted_text}")
        	else:
        		print("Invalid values has been provided\nExiting....")
        elif option ==2:
                fileName_encryptedtext = input("Enter the name of the file contaning the encrypted message: ")
                encrpted_text = read_Text(fileName_encryptedtext)
                key_value = int(input("Enter the value of key: "))
                shift_value = int(input("Enter the shift value: "))
                if valid_key_value(key_value) and valid_shift_value(shift_value):
                	print("\nProcess of decrypting the message has started. Please be patient....")
                	decrypted_text = decrypt(encrypted_text, key_value, shift_value)
                	print("Message has been successfully decrypted !!")
                	fileName_decrpytedText = input("Enter the name of the file in which decrypted text has to be written: ")
                	write_Text(fileName_decrpytedText, decrypted_text)
                	print(f"\nFollowing is the value of key, shift and decrpted text:\nKey Value: {key_value}\nShift Value: {shift_value}\nDecrypted Text: {decrypted_text}")
                else:
                	print("Invalid values has been provided\nExiting....")
                




