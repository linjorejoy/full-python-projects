from Image import Image
from Tags import Tags
from Album import Album
import os
import json

print()
image_dict = dict()

directory = os.path.abspath("images")
current_id = 1

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        this_img = Image(os.path.join(directory, filename))
        this_img.id = current_id
        image_dict[current_id] = this_img.__dict__
        current_id += 1


with open("images.json", "w") as json_file:
    json.dump(obj=image_dict, fp=json_file, indent=2)
