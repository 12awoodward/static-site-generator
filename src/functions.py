from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        inside_delim = False
        new_txt = ""
        for char in node.text:
            new_txt += char
            if new_txt[-len(delimiter):] == delimiter:
                new_txt = new_txt[:-len(delimiter)]
                if inside_delim:
                    new_nodes.append(TextNode(new_txt, text_type, node.url))
                else:
                    new_nodes.append(TextNode(new_txt, TextType.NORMAL, node.url))
                inside_delim = not inside_delim
                new_txt = ""

        if inside_delim:
            raise Exception("missing closing delimiter from: " + new_txt)
        if len(new_txt) > 0:
            new_nodes.append(TextNode(new_txt, TextType.NORMAL, node.url))
    
    return new_nodes

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