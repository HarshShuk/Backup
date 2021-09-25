import os
import shutil
sorce=input("Enter Sorce Folder Name")
destination=input("Enter Destination Folder Name")
sorce=sorce+'/'
destination=destination+'/'
list_of_files=os.listdir(sorce)
for file in list_of_files:
    shutil.move((sorce+file),destination)