
#Encrypting with key provided 

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
	
def encrypt(filename,key):
	'''
	Function to encrypt specified key that has been located 

	'''
	f = Fernet(key)
	with open(filename,'rb') as file:
		file_read = file.read()

	encrypted_data = f.encrypt(file_read)

	with open(filename,'wb') as file_en:
		file_en.write(encrypted_data)

if __name__ == '__main__':
	logo = '''
	##########################################

			DEV~£eloh
		ENCRYPTION  KIT @[ #@@# ]

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
					print("Encrypting #........#{}".format(file))
					encrypt(file_paths,key)

	except FileNotFoundError:
		print("Invalid file path please enter as follows:(E:\\filekey.key)")
		sys.exit()
	


