#!/usr/bin/env python
import glob
import os

for file in glob.glob("*.png"):
    print "processing", file
    os.system("convert " + file + " " + file[:-4] + ".gif")
    os.system("convert " + file + " " + file[:-4] + ".eps")
