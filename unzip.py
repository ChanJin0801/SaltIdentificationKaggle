import zipfile as zf

files = zf.ZipFile("test.zip", 'r')
files.extractall('test')

files.close()