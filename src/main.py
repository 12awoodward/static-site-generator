from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def text_node_to_hmtl_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            txt = text_node.text[1:text_node.text.index("]")]
            href = text_node.text[text_node.text.index("(") + 1:-1]
            return LeafNode("a", txt, {"href": href})
        case TextType.IMAGE:
            txt = text_node.text[2:text_node.text.index("]")]
            src = text_node.text[text_node.text.index("(") + 1:-1]
            return LeafNode("img", "", {"src": src, "alt": txt})
        case _:
            raise Exception("invalid text type")

def main():
    test = TextNode("Some Text", TextType.NORMAL, "address.com/")
    print(test)

main()