#!/usr/bin/python
import shutil
import os
import re
destination = ""
test = ""
for root, dir, files in os.walk("."):
    for x in files:
        if x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".png"):
            destination = "/home/ENTERYOURUSERNAMEHERE/Pictures/Sorted"
            test = str(root) + "/" + x
            shutil.copy(test,destination)
            os.remove(test)
