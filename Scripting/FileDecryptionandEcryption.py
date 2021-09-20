#Locating with files to find files with their respective sizes
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:42:20 2020

@author: Dev~£eloh
@Working@Project@SpaceCadet

@@@@POWERFULL FILE ENCRYPTOR AND DECRYPTION OF OS FILES @@#######################

The script makes use of (Fernet Encryption(modern AES)(Symetrical Cryptographical encryption) .....:::)
Ensure to store the key in secure location to avoid losing the entire encrypted file system 

###################################################################################################################
				!!!!!!HANDLE WITH CARE THIS SCRIPT WITH CAUTION !!!!!!
			STEPPING IN THE LAND OF LANDMINES,DRAGONS AND DINOSURES WITH LASER GUNS .....
			THE SCRIPT CAN ENCRYPT THE ENTIRE FILE SYSTEM AND RESULT TO ENTIRE SYSTEM CRASHING(WINDOWS) AND USELESS 

###################################################################################################################
Functionality :(Algorithm :Working principles)
1.Choose option eithe to encrypt or decrypt
2.Specify the file extension type so as to be able to decrypt it appropriately..
3.specify the file location drive i.e (C:// or all directories to be encrypted)
4.Encrypt the files specified
5.Prompt to show percentage proceedings 
6.Prompt to show complete encryption of the files
7.Separate decryption file with the decryption key 
8.Specify the filename of the file that needs to be decrypted ....(Sort of Regex to search for filename specified and lookup)
9.Account for the time taken to obfuscate the files specified using date_time(modul)
10.Use argparse to make the script commandlneand helpfull

"""
import os
from cryptography.fernet import Fernet
import stat 
import time 
import sys

def write_key():
	"""
	Generate the Fernet cryptographic key and save the key the local directory in this scope

	"""
	key = Fernet.generate_key()
	#Now save the generated to the local directory file
	with open('Key.key','wb') as key_file:
		key_file.write(key)
def load_key(Key):
	"""
	loads the Key.key stored in this directory file to use for the encryption process

	"""
	with open(Key) as k:
		key = k.read()

	return key

def encrypt(filename,key):
	"""
	Provided a filename(str) and Key(bytes) it encrypts the file and writes it 

	"""
	f = Fernet(key)
	with open(filename,'rb') as file:
		#now read all the file data 
		file_data = file.read()

	#encrypted_data = f.encrypt(file_data)
	#proceed to encrypt the data in the file 
	encrypted_data = f.encrypt(file_data)
	#Now write the encrypted file to your file system
	with open(filename,'wb') as file:
		file.write(encrypted_data)

def decrypt(filename,key):
	"""
	Given filename(str) and key(bytes) ,it decrypts the file and writes it

	"""

	f = Fernet(key)
	with open(filename,'rb') as file:
		#read the encrypted data
		encrypted_data = file.read()
	#proceed to decrypt the file
	decrypted_data = f.decrypt(encrypted_data)
	#write the file to its original file format 
	with open(filename,"wb") as file:
		file.write(decrypted_data)

if __name__ == "__main__":

	encrypt_key = "J_S6h3CQ0LYDyOrAMQXii9uD1Mh33W1bVbYpDUzpz-8="
	logo = '''
	############################################################################################################
	.........  . . . . .     .          ...    ....    <<<<<>>>>>>>         
	 .          .             .            .     .		<<< KAA >>>>
	 .          .             .              .  .		<<< MACHO >>
	 .          .             .               ..		
	 ........   ........      .              .  .
	 .          .             .             .     . 
	 .          .             .            .       .
	 .          .........     . . . . .   ...    .... 

	 ######################^^^^^^^^^^^^^^^^^^^^^^^^^^^###########################################################

		 !!!!!!HANDLE WITH CARE THIS SCRIPT WITH CAUTION !!!!!!
	STEPPING IN THE LAND OF LANDMINES,DRAGONS AND DINOSURES WITH LASER GUNS .....

	THE SCRIPT CAN ENCRYPT THE ENTIRE FILE SYSTEM AND RESULT TO ENTIRE SYSTEM CRASHING(WINDOWS) AND USELESS 

	USAGE:
	========
	paths = i.e C:\\
	extemsion = .jpg/ or any other file extension
	option = choose to encrypt or decrypt option on the target file system 

	<<<<<<<<>>>>>>>>>>

		( ^   ^ )
		( 0 ^  0)
		  ( <> )

	<< MASKED JOINT >>

	<<<<<<<>>>>>>>>>>>

	#############################################################################################################

	'''
	print(logo)
	paths = input("Enter file paths to seek Folders#: ")
	#files = ('.jpg','.pdf','.png','.exe','.csv')
	#Future code to support multiple file encryptions in the file_paths
	extension = input('Enter File extension You need to encrypt@#:')
	print("###@@The Files will be completely encrypted be carefull###@@")
	#Parsing the arguments as commandline below
	option = input("Enter an option (encrypt | decrypt) :?###~#")

	for fold,subfold,filenames in os.walk(paths):
		for file in filenames:
			if file.endswith(extension):
				file_paths = os.path.join(fold,file)

				#os.chmod(file_paths,stat.S_) change file modification to allo read and write operations 
				if option == "encrypt":
					print("Encrypting these files ....\t\t\t {} ".format(file))
					encrypt(file_paths,encrypt_key)
				elif option == 'decrypt':
					print("Dncrypting....\t\t\t {} ".format(file))
					decrypt(file_paths,encrypt_key)
				else:
					break
					
	print("Process Complete || ::@Dev Mochama 2020 ::Project @~SpaceCadet:: ||")