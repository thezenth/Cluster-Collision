import os

# -- PURPOSE -- #
#
# To manage the movement of files into and out of dropbox and the creation of new folders.
#
# -- PURPOSE -- #

dropbox_location = "~/Dropbox/"

# Determine location of dropbox folder
#try:
#	dropbox_location = os.system(
#		"find ~/ -type f -name 'dropbox'"
#	)
#	print (dropbox_location)
#except ValueError:
#	print("Oops! I can't find your dropbox folder. Maybe you need to install the dropbox daemon?")
	
# Move file into dropbox
def move_to_dropbox(fileName, dest, findFile=True):
	file_location = ""
	if findFile:
		file_location = os.system(
			"find ~/ -name " + fileName
		)
	else:
		file_location = fileName

	cmdStr = "mv " + file_location + " " + dropbox_location
	os.system(cmdStr)

# Make new folder in dropbox
def make_folder_dropbox(fName, returnLocation=False):
	location = dropbox_location + fName
	cmdStr = "mkdir " + dropbox_location + fName
	os.system(cmdStr)
	if returnLocation:
		return location

# Move entire folder into dropbox
def move_folder_to_dropbox(folderName, destFolder=None):
	folder_location = ""
	dest_folder_location = ""
	if destFolder is None:
		# make new folder with same name
		dest_folder_location = make_folder_dropbox(folderName, True)
	else:
		# don't need to make new folder
		dest_folder_location = destFolder

	# move files recursively into dropbox folder
	cmdStr = "mv -r " + folder_location
        os.system(cmdStr)
