from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def main():
    test = TextNode("Some Text", TextType.NORMAL, "address.com/")
    print(test)

main()