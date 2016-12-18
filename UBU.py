import os
import sys
import shutil
import zipfile
import traceback

print ('Welcome to USB Backup Utility')
print ('Created by: TheCryptek')
print ('\nWhat directory would you like to back up?')
print ('Example: C:/users/user/Desktop/Folder')
backUp = raw_input('> ') # Files the user specified to back up
print ('\nWhere would you like to back these files up at?')
print ('Example USB Letter: E:/')
backDevice = raw_input('> ') # Device the user specified to save the back up on.
print ('\nName of the zip file you prefer?')
print ('Example: Backup.zip')
backZip = raw_input('> ') # The name of the zip file specified by the user
print ('\nBackup started...')
if not os.path.exists(backDevice + '/BackUp'): # If the BackUp folder doesn't exist on the device then
	os.mkdir(backDevice + 'BackUp') # Make the backup folder on usb device
backZip = zipfile.ZipFile(backZip, 'w') # Not sure what to say for lines 21 - 26
for dirname, subdirs, files in os.walk(backUp): 
	backZip.write(dirname)
	for filename in files:
		backZip.write(os.path.join(dirname, filename))
	backZip.close()
shutil.move(backZip, backDevice + '/BackUp') # Move the zip files created in working directory to the specified back up device -[ Something is wrong with this can't figure out what ]-
print('Backup finished.')