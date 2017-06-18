# -----------------------------------------------------
# --[ name       : USB Backup Utility
# --[ description: A simple python backup script
# --[ author     : TheCryptek
# --[ github page: https://github.com/TheCryptek/UBU
# --[ Version    : 0.3
# -----------------------------------------------------

import os
import sys
import zipfile
import traceback
import cryp

# Make colors an easier way to type
header = cryp.bcolors.HEADER
blue = cryp.bcolors.OKBLUE
green = cryp.bcolors.OKGREEN
warning = cryp.bcolors.WARNING
fail = cryp.bcolors.FAIL
endc = cryp.bcolors.ENDC
bold = cryp.bcolors.BOLD
underline = cryp.bcolors.UNDERLINE

cryp.clear()

# The Welcome screen.

print header + """

USB Backup Utility
 _   _ ____  _   _ 
| | | | __ )| | | |
| | | |  _ \| | | |
| |_| | |_) | |_| |
 \___/|____/ \___/

Created by TheCryptek
""" + endc

raw_input("Press enter to continue...")
cryp.clear()

# Obtain the directory the user wants to back up
print bold + "\nWhat directory would you like to back up?" + endc
print "Windows: C:/users/user/Desktop/folder"
print "Linux: /home/user/Desktop/Folder"
backUp = raw_input(fail + "> " + endc)
cryp.clear()

# Obtain the device the user wants to use
print bold + "\nWhere would you like to back these files up at?" + endc
print "Windows: E:/"
print "Linux: /media/user/device"
backDevice = raw_input(fail + "> " + endc)
cryp.clear()

# Obtain the name of the zip file the user wants to use
print bold + "\nName of the zip file you prefer?" + endc
print "Example: Backup.zip"
backZip = raw_input(fail + "> " + endc)
cryp.clear()

# Notify the user that the script has started.
print green + "\nBackup started..."
dest = backDevice + "/Backup"
cryp.space()


# Check if the backup folder exists, if not, then create it.
print warning + "Checking to see if " + dest + " exists."
if not os.path.exists(backDevice + '/Backup'):
	os.mkdir(backDevice + "/Backup")
	print warning + dest + " did not exist... We have created it."

# Check if the specified zip file exists, if so. Delete it.
print warning + "Checking for " + backZip
if os.path.exists(os.path.join(dest, backZip)):
	os.remove(os.path.join(dest, backZip))
	print warning + backZip + " existed, we have removed it to update it."

# Create the zip file and place it in the user specified device.
bkZip = zipfile.ZipFile(os.path.join(dest, backZip), 'w')
for dirname, subdirs, files in os.walk(backUp):
	#bkZip.write(dirname[len(backUp):])
	for filename in files:
		path = os.path.join(dirname, filename)
		#print(path, backUp)
		bkZip.write(path, os.path.join(backUp.split(',')[-1], path[len(backUp):]))
		#bkZip.write(os.path.join(dirname, filename))
bkZip.close()

# Notify the user that the backup has finished and where it was saved.
print green + "\nBackup finished, stored at " + dest + "/" + backZip + endc
cryp.space()
raw_input("Press enter to finish...")
cryp.clear()
