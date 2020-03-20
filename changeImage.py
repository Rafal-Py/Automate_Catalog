#!/usr/bin/env python3
import os, sys
from PIL import Image

path = "./supplier-data/images"
files = os.listdir(path)

size = (600, 400)

for file in files:
    if not file.endswith(".tiff"):
        continue
    infile = os.path.join(path, file)
    #print(infile)
    outfile = os.path.join(os.path.split(infile)[0], file[:-5]) + ".jpeg"
    #print(outfile)
    try:
        with Image.open(infile) as im:
            out = im.convert("RGB")
            out.thumbnail(size)
            out.save(outfile, "JPEG")
    except Exception as e:
        print(e)
        pass
