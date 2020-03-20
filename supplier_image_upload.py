#!/usr/bin/env python3
import os
import requests

path = "./supplier-data/images"
files = os.listdir(path)
url = http://35.225.146.151/

for file in files:
    if not file.endswith(".jpeg"):
        continue
    image = os.path.join(path, file)
    with open(image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
