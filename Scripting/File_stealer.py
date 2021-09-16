
'''
Ninja One Automation Script 
Coded by : Dev~Feloh
Project Motivation from @Project Space Cadet ::
Copies and able to move  files from a newly inserted storage device to an external defined location in the file system  
*def copy specific files from folder

'''
import shutil
import os
import time
import datetime 
import sys
import argparse

def create_folder(path,name):
	#Check is path exists and create a new directory if none of same name exists:
	os.chdir(path)
	#now create a Folder in the specified paths ..
	try:
		os.mkdir(name)
	except FileExistsError:
		print("The folder Allready  Exists in the path")
	pathing = os.path.join(path,name)
	return pathing

def scrape_files(path):
    os.chdir(path)
    print("Enter the Destination FolderPath:\n")
    folderpath = input("Dev~£eloh#: ")
    print("Enter the Destination Folder Name ")
    foldername = input("Dev~£eloh#: ")
    destination = create_folder(folderpath,foldername)
    commonfiles = input("Enter the file type to scrape :@##")

    try:
        sttime = time.time()
        counter = 0
        for folder,subfolder,filenames in os.walk(path):
                for filess in filenames:
                    
                    if filess.endswith(commonfiles):
                        
                        shutil.copy(os.path.join(folder,filess),destination)
                        size = os.path.getsize(os.path.join(folder,filess))
                        print("Copying Please Wait ...",counter,'\t',filess,'\t',size,'Bytes')
                        counter += 1
        endtime = time.time()
        timer = endtime - sttime
        print("Execution  Time in :",round(timer,3),"Seconds :Procedure complete Buddy :::")
        print(datetime.datetime.now())
        print("THANKS BUDDY ")
        print("Your files were copied to :{} in folder: {} ".format(folderpath,destination))

    except OSError:
       print("There is no space left in your device :")
    except KeyboardInterrupt:
        sys.exit()
    
   

if __name__ == '__main__':
	os.system('color a')
	logo = '''
	 .........  . . . . .     .          ...    ....    <<<<<>>>>>>>         
	 .          .             .            .     .		<<< KAA >>>>
	 .          .             .              .  .		<<< MACHO >>
	 .          .             .               ..		
	 ........   ........      .              .  .
	 .          .             .             .     . 
	 .          .             .            .       .
	 .          .........     . . . . .   ...    .... 
	 USAGE ::
	Enter filepaths as :: F:\\ and filenames as you wish i.e feloh,james,githurai e.t.c 
	===================================================================================
	-----------------------------------------------------------------------------------
	@#@#@#@~~~~~~~~###############################~~~~~~~~~~~~~~~~~~@@@@##

	@Dev~£eloh || 2020 || Enjoy  Automation Project ||SPACE $$ CADET ||.

	@#@#@#@~~~~~~~~###############################~~~~~~~~~~~~~~~~~~@@@@##
	-----------------------------------------------------------------------------------
	===================================================================================
	'''
	print(logo)
	print("Enter the Path you want to Scan for Files to Steal :")
	filepath = input("Dev~£eloh#: ")
	scrape_files(filepath)