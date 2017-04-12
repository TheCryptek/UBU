def zip()
	bkZip = zipfile.ZipFile(os.path.join(dest, backZip), 'w')
	for dirname, subdirs, files in os.walk(backUp):
		bkZip.write(dirname)
		for filename in files:
			bkZip.write(os.path.join(dirname, filename))
	bkZip.close()
