import os
import hashlib
from collections import defaultdict
##handling items from the collections module of python programming language 
items = []
def digest(filename):
	chunksize = 1024
	hashe = hashlib.md5()
	with open(filename,"rb") as digster:
		chunk = digster.read(chunksize)
		while True:
			chunk = digster.read(chunksize)
			if not chunk:
				break
			hashe.update(chunk)
            
			##returning hexdigest object checksum from the object that has been read
	return hashe.hexdigest()

def store_duplicates(path):
	#identifying duplicates from the filesystem digests
	global items
	for fold,subfold,filenames in os.walk(path):
		for file in filenames:
			file_paths = os.path.join(fold,file)
			#append the items to the list of complementary items in the list of items
			items.append(digest(file_paths))
	counter = 0
	with open("hell.txt","w") as  writer:
		for it in items:
			writer.write(it + "\n")

def find_duplicates():
	##checking for duplicate items from the list of items from the generated checksum of objects in items
	for it in items:
		print(it)

	#now returning items from the list of items 
if __name__ == '__main__':
	##trying to read from file stored in the device specified below 
	path = r""
	store_duplicates(path)
	find_duplicates()
