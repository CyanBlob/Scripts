#!/usr/bin/python
import shutil
import os
import re
source = os.listdir("/home/andrew-arch/Downloads")
destination = "/home/andrew-arch/Documents"
test = ""
for files in source:
    if files.endswith(".txt") or files.endswith(".pdf") or files.endswith(".doc") or files.endswith(".docx") or files.endswith(".odt") or files.endswith(".xlsx"):
            destination = "/home/andrew-arch/Documents/Downloaded"
            test = "/home/andrew-arch/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)
    
    elif files.endswith(".mp3") or files.endswith(".m4a") or files.endswith(".wav") or files.endswith(".pdf"):
            destination = "/home/andrew-arch/Music/Downloaded"
            test = "/home/andrew-arch/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)

    elif files.endswith(".avi") or files.endswith(".mpg") or files.endswith(".mkv") or files.endswith(".divx") or files.endswith(".vob") or files.endswith(".mp4") or files.endswith(".m4v"):
            destination = "/home/andrew-arch/Videos/Downloaded"
            test = "/home/andrew-arch/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)
    
    elif files.endswith(".jpg") or files.endswith(".jpeg") or files.endswith(".png") or files.endswith(".raw") or files.endswith(".gif") or files.endswith(".bmp"):
            destination = "/home/andrew-arch/Pictures/Downloaded"
            test = "/home/andrew-arch/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)
       
    elif files.endswith(".torrent") or files.endswith(".iso"):
            destination = "/home/andrew-arch/Downloads/Torrents"
            test = "/home/andrew-arch/Downloads/" + files
            shutil.copy(test,destination)
            os.remove(test)
