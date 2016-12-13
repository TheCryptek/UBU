#!/usr/bin/python
#
#
import os
import sys
import shutil
import zipfile
import traceback

backFiles = 'E:/UniBrute'
BP = 'E:/BackUp'
print ("Welcome to USB Backup Utiltiy")
print ("Created by: TheCryptek")

print ("""
		[1] Backup files to USB
		[2] Restore files from USB
	   """)
ans = raw_input ("What would you like to do? ")

if ans == "1":
	print ("Starting the backup.")
	if not os.path.exists(BP):
		os.mkdir(BP)
	if os.path.exists(backFiles):
		shutil.rmtree(backFiles)
	shutil.copytree ('C:/Users/TheCryptek/Desktop/UniBrute', 'E:/UniBrute')
	backZip = zipfile.ZipFile('E:\BackUp\UniBrute.zip', 'w')
	for dirname, subdirs, files in os.walk(backFiles):
		backZip.write(dirname)
		for filename in files:
			backZip.write(os.path.join(dirname, filename))
		backZip.close()
	shutil.rmtree('E:/UniBrute')
	print ("Backup finished.")