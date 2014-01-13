#!/usr/bin/python
import shutil
import os
import re
destination = ""
test = ""
path = ""
for root, dir, files in os.walk("."):
    for x in files:
        if x.endswith(".txt") or x.endswith(".pdf") or x.endswith(".doc") or x.endswith(".docx") or x.endswith(".odt") or x.endswith(".xlsx"):
            destination = "/home/andrew-arch/Documents/Downloaded"
            test = str(root) + "/" + x
            shutil.copy(test,destination)
            os.remove(test)
    
        elif x.endswith(".mp3") or x.endswith(".m4a") or x.endswith(".wav") or x.endswith(".pdf"):
            destination = "/home/andrew-arch/Music/Downloaded"
            test = str(root) + "/" + x
            shutil.copy(test,destination)
            os.remove(test)

        elif x.endswith(".avi") or x.endswith(".mpg") or x.endswith(".mkv") or x.endswith(".divx") or x.endswith(".vob") or x.endswith(".mp4") or x.endswith(".m4v"):
            destination = "/home/andrew-arch/Videos/Downloaded"
            test = str(root) + "/" + x
            shutil.copy(test,destination)
            os.remove(test)
    
        elif x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".png") or x.endswith(".raw") or x.endswith(".gif") or x.endswith(".bmp"):
            destination = "/home/andrew-arch/Pictures/Downloaded"
            test = str(root) + "/" + x
            shutil.copy(test,destination)
            os.remove(test)
       
        elif x.endswith(".torrent") or x.endswith(".iso"):
            destination = "/home/andrew-arch/Downloads/Torrents"
            test = str(root) + "/" + x
            shutil.copy(test,destination)
            os.remove(test)
