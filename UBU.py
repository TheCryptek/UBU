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
import pizza

# The Welcome screen.

print """

USB Backup Utility
 _   _ ____  _   _ 
| | | | __ )| | | |
| | | |  _ \| | | |
| |_| | |_) | |_| |
 \___/|____/ \___/

Created by TheCryptek
"""

# Obtain the directory the user wants to back up
print "\nWhat directory would you like to back up?"
print "Windows: C:/users/user/Desktop/folder"
print "Linux: /home/user/Desktop/Folder"
backUp = raw_input("> ")

# Obtain the device the user wants to use
print "\nWhere would you like to back these files up at?"
print "Windows: E:/"
print "Linux: /media/user/device/"
backDevice = raw_input("> ")

# Obtain the name of the zip file the user wants to use
print "\nName of the zip file you prefer?"
print "Example: Backup.zip"
backZip = raw_input("> ")

# Notify the user that the script has started.
print "\nBackup started..."
dest = backDevice + "/BackUp"

# Check if the backup folder exists, if not, then create it.
if not os.path.exists(backDevice + '/BackUp'):
	os.mkdir(backDevice + "BackUp")

# Check if the specified zip file exists, if so. Delete it.

if os.path.exists(os.path.join(dest, backZip)):
	os.remove(os.path.join(dest, backZip))

# Create the zip file and place it in the user specified device.
bkZip = zipfile.ZipFile(os.path.join(dest, backZip), 'w')
for dirname, subdirs, files in os.walk(backUp):
	bkZip.write(dirname)
	for filename in files:
		bkZip.write(os.path.join(dirname, filename))
bkZip.close()

# Notify the user that the backup has finished and where it was saved.
print "\nBackup finished, stored at " + dest + "/" + backZip
