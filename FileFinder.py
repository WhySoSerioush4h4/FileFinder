# ***Some Codes were found from Stack Overflow and GeeksForGeeks.org and used for reference to better understand any modules used***

# Gabriel Romano
# ---Redacted---
# ---Redacted---
import os
import os.path
 
startDir = input('Enter the start directory: ')
string = input('Enter the String you are looking for: ')
target = input('Enter the target file along with any extension: ')
 
 
def searchfile(filename):
    for root, dirs, files in os.walk(startDir):
        print('Looking in:', root)
        for Files in files:
            try:
                found = Files.find(filename)
                print(found)
                if found != -1:
                    print(filename, 'Found')
                    readfile(target)
            except:
                exit
 
 
def readfile(filename):
    # opening a text file
    file1 = open(target, "r")
    print('Opening', filename, '...')
    # read file content
    readfile = file1.read()
    print('Reading', filename, '...')
    # checking condition for string found or not
    if string in readfile:
        print('String', string, 'Found In File')
        # closing the file
        file1.close()
    else:
        print('String', string, 'Not Found')
 
 
searchfile(target)
readfile(target)
