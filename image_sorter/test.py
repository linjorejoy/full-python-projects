import json
import os

loc = input("Address : ")


for folder in os.listdir(loc):

    print(os.path.isdir(os.path.join(loc, folder)), "\t", folder)
