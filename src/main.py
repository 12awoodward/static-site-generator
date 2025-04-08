from file_functions import *

def main():
    copy_files("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")

main()