#Password extractor script using python
#Script to locate all saved wifi passwords and encrypt down the password and save the encrypted passwords to C:\\

import subprocess
import os
from cryptography.fernet import Fernet
import getpass
import shutil
##commandline script to find all local wifi passwords in a windows pc
##while decoding avoid UnicodeDecodeError with a errors='replace' statement while decoding the python script

data = subprocess.check_output(['netsh','wlan','show','profile']).decode('utf-8',errors='replace').split('\n')
#print(data)
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

user = getpass.getuser()

file = open(f"C:\\Users\\{user}\\Downloads\\pswds.txt","w")

for i in profiles:
	password = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8',errors='replace').split('\n')
	items = [b.split(':')[1][1:-1] for b in password if "Key Content" in  b]

	# Now printing available wifi networks with their passwords to console 
	try:
		file.write("{} ,'\t\t\t\t ' {}".format(i,items[0]) + "\n\n")
	except IndexError:
		##print("index error")
		file.write("{} ,'\t\t\t', {}".format(i,"Free Network :No Password :") + "\n\n")
file.close()

key = "J_S6h3CQ0LYDyOrAMQXii9uD1Mh33W1bVbYpDUzpz-8="

f = Fernet(key)

with open(f"C:\\Users\\{user}\\Downloads\\pswds.txt","rb") as ff:
	file_toencrypt = ff.read()
    
encrypted_data = f.encrypt(file_toencrypt)
with open(f"C:\\Users\\{user}\\Downloads\\pswds.txt","wb") as fr:
	fr.write(encrypted_data)


print("Operation Completed:")
dst = input("Enter the Destination Folder:")
src = f"C:\\Users\\{user}\\Downloads\\pswds.txt"  
try:
    shutil.move(src,dst)
except:
    print("File Allready exists in destination delete or move to new location:")
    os.unlink(src)
    








