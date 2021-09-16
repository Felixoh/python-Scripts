##Project to Locate a given file in a windows with many drives ("Change extension to desired Extension")
import os
import subprocess
import shutil
import stat

#Run external command to find all logicaldisks before going through each logicall drive to locate all the items 
cmd = subprocess.check_output(['wmic','logicaldisk','get','name']).decode('utf-8',errors='replace').split(':')

##save all the drive_letters as a list of items 
drive_letters  = [d.split('\n')[1]for d in cmd]

#append all the filepaths to the list shown below  before  locating th files we need to find in the filesystem
file_paths = []

common_files = ('.docx','.pptx')
for item in drive_letters:
	#iterate over the logical drive individually locating the specified file
	paths = item + ":" + r"\\"
	#allow the programme to take breaks if five at each drive instance 
	#logic to locate all the files in .pdf
	for fold,subfold,filenames in os.walk(paths):
		for files in filenames:
			if files.endswith(common_files):
				#print("Analysing {}".format(files))
				pathing = os.path.join(fold,files)
				file_paths.append(pathing)
                
#pretty print available filepaths in the stored list if items 
dst = input("Enter the Destination Folder:")
for i in file_paths:
	##print(available logical drives in the partition)
    try:
        shutil.copy(i,dst)
        print("Copying please wait:")
    except PermissionError:
        pass
    except shutil.Error:
        pass

print("Process Completed Successfully:")
