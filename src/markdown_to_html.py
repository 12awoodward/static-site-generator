from parentnode import ParentNode
from textnode import TextNode, TextType
from inline_functions import text_to_textnodes, text_node_to_hmtl_node
from block_functions import markdown_to_blocks, block_to_block_type, BlockType


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode("div", [])

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                parent.add_child(paragraph_to_html_node(block))
            case BlockType.HEADING:
                parent.add_child(heading_to_html_node(block))
            case BlockType.CODE:
                parent.add_child(code_to_html_node(block))
            case BlockType.QUOTE:
                parent.add_child(quote_to_html_node(block))
            case BlockType.UNORDERED_LIST:
                parent.add_child(u_list_to_html_node(block))
            case BlockType.ORDERED_LIST:
                parent.add_child(o_list_to_html_node(block))
            case _:
                raise Exception("invalid block type")

    return parent


def paragraph_to_html_node(markdown: str):
    text_nodes = text_to_textnodes(markdown.replace("\n", " "))
    paragraph = ParentNode("p", [])
    for node in text_nodes:
        paragraph.add_child(text_node_to_hmtl_node(node))
    return paragraph


def heading_to_html_node(markdown: str):
    separated = markdown.split(" ", 1)
    tag = "h" + str(len(separated[0]))
    text_nodes = text_to_textnodes(separated[1])
    heading = ParentNode(tag, [])
    for node in text_nodes:
        heading.add_child(text_node_to_hmtl_node(node))
    return heading


def code_to_html_node(markdown: str):
    child = text_node_to_hmtl_node(TextNode(markdown[3:-3].lstrip(), TextType.NORMAL))
    return ParentNode("pre", [ParentNode("code", [child])])


def quote_to_html_node(markdown: str):
    lines: list[str] = []

    for line in markdown.split("\n"):
        parts = line.split(" ", 1)
        if len(parts) == 1:
            lines.append("&nbsp;")
        else:
            lines.append(parts[1])

    markdown = " ".join(lines)
    text_nodes = text_to_textnodes(markdown.replace("> ", ""))
    quote = ParentNode("blockquote", [])

    for node in text_nodes:
        quote.add_child(text_node_to_hmtl_node(node))
    return quote


def u_list_to_html_node(markdown: str):
    list_items = markdown.split("\n")
    u_list = ParentNode("ul", [])
    for item in list_items:
        u_list.add_child(list_item_to_html_node(item[2:]))
    return u_list


def o_list_to_html_node(markdown: str):
    list_items = markdown.split("\n")
    o_list = ParentNode("ol", [])
    for item in list_items:
        o_list.add_child(list_item_to_html_node(item.split(" ", 1)[1]))
    return o_list


def list_item_to_html_node(item: str):
    text_nodes = text_to_textnodes(item)
    list_item = ParentNode("li", [])
    for node in text_nodes:
        list_item.add_child(text_node_to_hmtl_node(node))
    return list_item
