import os
import hashlib

#contstruct global has object
h = hashlib.sha256()

# traverse the files
for root, dirs, files in os.walk("."):
    #go through roots dirs files and splits them
    path = root.split(os.sep)
    #prints base of root file
    print((len(path) - 1) * '/', os.path.basename(root))
    #prints the indidual file and hashes it
    for file in files:
        print(len(path) * '/', file)
        #if file cannot be hased end else hash file
        haslib.sha256(file)
        #update it to the hash lib
        h.update(.encode)


#sources
#https://docs.python.org/3/library/hashlib.html
#https://stackoverflow.com/questions/16953842/using-os-walk-to-recursively-traverse-directories-in-python
