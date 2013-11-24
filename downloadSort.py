#!/usr/bin/python
import shutil
import os
import re
source = os.listdir("/home/andrew-fedora/Downloads")
destination = "/home/andrew-fedora/Documents"
test = ""
for files in source:
    if files.endswith(".txt") or files.endswith(".pdf") or files.endswith(".doc") or files.endswith(".docx") or files.endswith(".odt") or files.endswith(".xlsx"):
            print files
            destination = "/home/andrew-fedora/Documents"
            test = "/home/andrew-fedora/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)
    
    elif files.endswith(".mp3") or files.endswith(".m4a") or files.endswith(".wav") or files.endswith(".pdf"):
            print files
            destination = "/home/andrew-fedora/Music"
            test = "/home/andrew-fedora/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)

    elif files.endswith(".avi") or files.endswith(".mpg") or files.endswith(".mkv") or files.endswith(".divx") or files.endswith(".vob") or files.endswith(".mp4") or files.endswith(".m4v"):
            print files
            destination = "/home/andrew-fedora/Videos"
            test = "/home/andrew-fedora/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)
    
    elif files.endswith(".jpg") or files.endswith(".jpeg") or files.endswith(".png") or files.endswith(".raw") or files.endswith(".gif") or files.endswith(".bmp"):
            print files
            destination = "/home/andrew-fedora/Pictures"
            test = "/home/andrew-fedora/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)
    
