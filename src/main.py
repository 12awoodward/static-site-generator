from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from inline_functions import *
from block_functions import *

import os
import shutil

def copy_files(origin, destination):
    if not(os.path.exists(origin) and os.path.exists(destination)):
        raise Exception("invalid file location")
    
    if len(os.listdir(destination)) > 0:
        shutil.rmtree(destination)
        os.mkdir(destination)
    
    for item in os.listdir(origin):
        item_path = os.path.join(origin, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
        else:
            new_dst = os.path.join(destination, item)
            os.mkdir(new_dst)
            copy_files(item_path, new_dst)

def main():
    copy_files("static", "public")

main()