from file_functions import *

import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_files("static", "public")

    generate_pages_recursive("content","template.html", "public", basepath)

main()