#!/usr/bin/python
#
#
import os
import sys
import shutil
import zipfile
import traceback


backFiles = 'E:/UniBrute'
#backUp = 'E:/BackUp'
backZip = 'E:/BackUp/UniBrute.zip'
zipName = 'UniBrute.zip'
#save = 'C:/users/TheCryptek/Desktop/UniBrute'

print ("Welcome to USB Backup Utiltiy")
print ("Created by: TheCryptek")

print ("""
		[1] Backup files to USB
		[2] Restore files from USB
	   """)
ans = raw_input ("What would you like to do? ")

if ans == "1":
	
	print ("\nWhat directory would you like to back up?")
	print ("Example: C:/user/user/Desktop/Folder")
	save = raw_input("> ")
	print ("\nWhere would you like it to be backed up?")
	backUp = raw_input("> ")
	
	print (save + backUp) #Debug Purposes
#	print ("Starting the backup.")
#	if not os.path.exists(BackUp):
#		os.mkdir(BackUp)
#	if os.path.exists(backFiles):
#		shutil.rmtree(backFiles)
#	if os.path.exists(backZip):
#		os.unlink(backZip)
#	shutil.copytree ('C:/Users/TheCryptek/Desktop/UniBrute', 'E:/UniBrute')
#	backZip = zipfile.ZipFile('E:\BackUp\UniBrute.zip', 'w')
#	for dirname, subdirs, files in os.walk(backFiles):
#		backZip.write(dirname)
#		for filename in files:
#			backZip.write(os.path.join(dirname, filename))
#		backZip.close()
#	shutil.rmtree(backFiles)
#	print ("Backup finished.")