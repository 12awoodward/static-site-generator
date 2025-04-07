from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from inline_functions import *
from block_functions import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode("div", [])

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                parent.children.append(paragraph_to_html_node(block))
            case BlockType.HEADING:
                parent.children.append(heading_to_html_node(block))
            case BlockType.CODE:
                parent.children.append(code_to_html_node(block))
            case BlockType.QUOTE:
                parent.children.append(quote_to_html_node(block))
            case BlockType.UNORDERED_LIST:
                parent.children.append(u_list_to_html_node(block))
            case BlockType.ORDERED_LIST:
                parent.children.append(o_list_to_html_node(block))
            case _:
                raise Exception("invalid block type")
            
    return parent

def paragraph_to_html_node(markdown):
    text_nodes = text_to_textnodes(markdown.replace("\n"," "))
    paragraph = ParentNode("p", [])
    for node in text_nodes:
        paragraph.children.append(text_node_to_hmtl_node(node))
    return paragraph

def heading_to_html_node(markdown):
    separated = markdown.split(" ", 1)
    tag = "h" + str(len(separated[0]))
    text_nodes = text_to_textnodes(separated[1])
    heading = ParentNode(tag, [])
    for node in text_nodes:
        heading.children.append(text_node_to_hmtl_node(node))
    return heading

def code_to_html_node(markdown):
    child = text_node_to_hmtl_node(TextNode(markdown[3:-3].lstrip(), TextType.NORMAL))
    return ParentNode("pre", [ParentNode("code", [child])])

def quote_to_html_node(markdown):
    text_nodes = text_to_textnodes(markdown.replace("> ", "").replace("\n"," "))
    quote = ParentNode("blockquote", [])
    for node in text_nodes:
        quote.children.append(text_node_to_hmtl_node(node))
    return quote

def u_list_to_html_node(markdown):
    list_items = markdown.split("\n")
    u_list = ParentNode("ul", [])
    for item in list_items:
        u_list.children.append(list_item_to_html_node(item[2:]))
    return u_list

def o_list_to_html_node(markdown):
    list_items = markdown.split("\n")
    o_list = ParentNode("ol", [])
    for item in list_items:
        o_list.children.append(list_item_to_html_node(item.split(" ", 1)[1]))
    return o_list

def list_item_to_html_node(item):
    text_nodes = text_to_textnodes(item)
    list_item = ParentNode("li", [])
    for node in text_nodes:
        list_item.children.append(text_node_to_hmtl_node(node))
    return list_item