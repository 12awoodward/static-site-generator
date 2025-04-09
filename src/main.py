from file_functions import *

def main():
    copy_files("static", "public")

    generate_pages_recursive("content","template.html", "public")

main()