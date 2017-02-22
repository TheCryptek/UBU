import os
import sys
import shutil
import zipfile
import traceback

print ('Welcome to USB Backup Utility')
print ('Created by: TheCryptek')
print ('\nWhat directory would you like to back up?')
print ('Windows: C:/users/user/Desktop/Folder')
print ('Linux: /home/user/Desktop/Folder')
backUp = raw_input('> ') # Files the user specified to back up
print ('\nWhere would you like to back these files up at?')
print ('Windows: E:/')
print ('Linux: /media/user/device/')
backDevice = raw_input('> ') # Device the user specified to save the back up on.
print ('\nName of the zip file you prefer?')
print ('Example: Backup.zip')
backZip = raw_input('> ') # The name of the zip file specified by the user
print ('\nBackup started...')
dest = backDevice + '/BackUp'

if not os.path.exists(backDevice + '/BackUp'): # If the BackUp folder doesn't exist on the device then
	os.mkdir(backDevice + 'BackUp') # Make the backup folder on specified back up device

bkZip = zipfile.ZipFile(os.path.join(dest, backZip), 'w') # Not sure what to say for lines 26 - 31

for dirname, subdirs, files in os.walk(backUp):
	bkZip.write(dirname)
	for filename in files:
		bkZip.write(os.path.join(dirname, filename))
bkZip.close()

print('\nBackup finished, stored at ' + dest + '/' + backZip)
