from file_functions import *

import sys

def build_site(static_files, content_files, template, destination, basepath):
    if not(os.path.exists(static_files) and os.path.exists(content_files) and os.path.exists(template)):
        raise Exception("invalid file path")
    
    if not(os.path.exists(destination)):
        os.mkdir(destination)
    elif len(os.listdir(destination)) > 0:
        shutil.rmtree(destination)
        os.mkdir(destination)

    copy_files(static_files, destination)
    generate_pages_recursive(content_files, template, destination, basepath)

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    static_files_dir = "static"
    content_files_dir = "content"
    template_file = "template.html"
    dest_dir = "docs"

    build_site(static_files_dir, content_files_dir, template_file, dest_dir, basepath)

main()