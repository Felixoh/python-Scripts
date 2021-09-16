
#Decrypting filesystem  with provided Key 
#Thhe DEcryption key needs to be stored in a different location if necessary 
import os
from cryptography.fernet import Fernet 
import sys

def load_key(location):
	'''
	load key from storage system i.e H:\\key.key
	'''
	with open(location,'rb') as rd:
		key = rd.read()
	return key

def decrypt(filename,key):

	f = Fernet(key)
	with open(filename,'rb') as file:
		encrypted_data = file.read()

	decrypted_data = f.decrypt(encrypted_data)
	
	with open(filename,'wb') as file_en:
		file_en.write(decrypted_data)


if __name__ == '__main__':
	logo = '''
	##########################################

			DEV~£eloh
		DECRYPTION KIT@#######

	##########################################

	'''
	print(logo)

	try:
		location = input("Enter key location path#~#£:")
		key = load_key(location)
		path = input("Enter the File location path you need to scrape ::")
		extension = input("Enter the File extension :##@@::")

		for fold,subfold,filenames in os.walk(path):
			for file in filenames:
				if file.endswith(extension):
					file_paths = os.path.join(fold,file)
					print("Decrypting #........#{}".format(file))
					decrypt(file_paths,key)

	except FileNotFoundError:
		print("Invalid file path please enter as follows:(E:\\filekey.key)")
		sys.exit()