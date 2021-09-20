# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:50:57 2020

@author: Dev~£eloh

python script to walk through  a folder and find similar files and delete them

"""
import os
import hashlib
from collections import defaultdict

src_folder = "C:\\Users\\Administrator\\Desktop\\BST BKS" 

def generate_md5(fname,chunksize=1024):
    """
    check the checksum of a file and return the md5 checksum of the file

    """
    hashe = hashlib.md5()
    with open(fname,'rb') as f:
        chunk  = f.read(chunksize)
        #keep reading and updating the chunk size until the end
        while True:
            chunk = f.read(chunksize)
            if not chunk:
                break
            hashe.update(chunk)

    #now return the hexdigest checksum
    return hashe.hexdigest()

if __name__ == '__main__':
    md5dict = defaultdict(list)
    filetypes  = ['pdf','exe','json']

    #walk throgh all the files of the files in a directory to find all files with similar checksum hence the files
    #shows all redudant files in the filepaths 

    for path,dirs,files in os.walk(src_folder):
        print("Analyzing the folder strsucture {} ".format(path))
        for each_file in files:
            if each_file.split('.')[-1].lower() in filetypes:
                file_path = os.path.join(os.path.abspath(path),each_file)
                #check for files having the same checksum 
                md5dict[generate_md5(file_path).append(file_path)]

    duplicate_values = (val for key,val in md5dict.items() if len(val) > 1 )
    print(duplicate_values)
