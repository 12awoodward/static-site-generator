from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from inline_functions import *
from block_functions import *

def main():
    test = TextNode("Some Text", TextType.NORMAL, "address.com/")
    print(test)

main()