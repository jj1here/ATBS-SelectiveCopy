#! python3
# walks through a folder tree and finds a certain extension and copy the files into a new folder.

import os, shutil, re, pathlib
from typing import Counter

def selectCopy(extent, path) :

    # creates new folder
    newFolder = f"{os.getcwd()}/copyOf({extent})s"
    # if the folder does not exist it creates one
    if not os.path.exists(newFolder) :
        os.makedirs(newFolder)


    findRegex = re.compile(rf"""
        (.+){extent} #finds the extension
    """, re.VERBOSE)
    
    count = 0 #keeps track of how many files copied

    #walks through the directory
    for folder, subfolders, files in os.walk(path) :
        
        #Looks at each file
        for file in files :
            # searches the file for the extension
            mo = findRegex.search(file)
            # if not found starts the loop over
            if mo == None :
                continue
            # if found count + 1
            count += 1
            # copies the file to the newfolder
            found = f"{path}/{file}" #creates the correct path for the file
            shutil.copy(found, newFolder)

    # if the count is 0 the program did not find any files and removes the new folder
    if count == 0:
        print(f"Sorry could not find any files with the extension {extent}")
        os.rmdir(newFolder)
    
    # message summarizing what happended
    elif count != 0 :
        print(f"We found {count} files with the extenstion {extent} and put them in the folder '{pathlib.Path(newFolder).name}'")
    # end of function

# gets extension
print("What extension (.jpg, .txt, etc.) would you like to copy?")
extent = input()

# gets folder/directory to check
print("In what folder/directory would you like to copy from?")
pathing = os.path.abspath(input())

# activates function
selectCopy(extent, pathing)