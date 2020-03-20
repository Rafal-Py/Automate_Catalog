#!/usr/bin/env python3
import os
import requests
import json

path = "./supplier-data/descriptions/"
files = os.listdir(path)
descriptions = []

for file in files:
    with open(os.path.join(path,file)) as f:
        lines = f.readlines()
        descriptions.append({"name": lines[0].strip(),
                            "weight": int(lines[1].strip().strip(' lbs')),
                            "description": lines[2].strip(),
                            "image_name": file[:-4] + ".jpeg"})

for description in descriptions:
    r = requests.post("http://35.225.146.151/fruits/", data = description)
    print(r.raise_for_status())

with open('descriptions.json', 'w') as desc_json:
    json.dump(descriptions, desc_json, indent = 4)
