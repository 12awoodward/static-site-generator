from textnode import *
from leafnode import *

import re

def text_to_textnodes(text):
    delim_types = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]

    result = split_nodes_link(split_nodes_image([TextNode(text, TextType.NORMAL)]))
    for delim, type in delim_types:
        result = split_nodes_delimiter(result, delim, type)

    return result

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)

        for image in images:
            sections = node.text.split(f"![{image[0]}]({image[1]})")

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            node.text = sections[1]
        
        if node.text:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)

        for link in links:
            sections = node.text.split(f"[{link[0]}]({link[1]})")

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            node.text = sections[1]
        
        if node.text:
            new_nodes.append(node)
    return new_nodes

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
                if inside_delim and len(new_txt) > 0:
                    new_nodes.append(TextNode(new_txt, text_type))
                elif not(inside_delim) and len(new_txt) > 0:
                    new_nodes.append(TextNode(new_txt, TextType.NORMAL))
                inside_delim = not inside_delim
                new_txt = ""

        if inside_delim:
            raise Exception("missing closing delimiter from: " + new_txt)
        if len(new_txt) > 0:
            new_nodes.append(TextNode(new_txt, TextType.NORMAL))
    
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
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text type")