import os
import shutil

# Copy photos to <sourcePath>
# Run <sourcePath> through ExifRenamer
# Run this script

sourcePath = "/Volumes/Data/foton sorterade/tmp"
targetPath = "/Volumes/Data/foton sorterade" 

def createFolder(name):
	if not os.path.exists(name):
		print("+", os.path.split(name))
		os.mkdir(name)


for dirpath, dirnames, filenames in os.walk(sourcePath):
	print("processing", dirpath)
	for filename in filenames:
		substrings = filename.split('-', 2)
		
		if os.path.isfile(os.path.join(dirpath,filename)) and len(substrings)>1:
			year = os.path.join(targetPath, substrings[0])
			createFolder(year)
			month = os.path.join(year, substrings[1]) 
			createFolder(month)
			shutil.move(os.path.join(dirpath, filename), os.path.join(month, filename))
	
	files = os.listdir(dirpath)
	if len(files)==0:
		os.rmdir(dirpath)
        
