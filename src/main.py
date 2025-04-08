from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from inline_functions import *
from block_functions import *
from markdown_to_html import *

import os
import shutil

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    write_file(dest_path, html_page)


def read_file(path):
    with open(path, "r") as file:
        return file.read()
    
def write_file(path, content):
    file_dir = os.path.dirname(path)
    if not os.path.exists:
        os.makedirs(file_dir)
    
    with open(path, "w") as file:
        file.write(content)

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

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.split(" ", 1)[1].strip()
    raise Exception("no h1 header")

def main():
    copy_files("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")

main()