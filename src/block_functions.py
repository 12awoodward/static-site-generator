from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph block"
    HEADING = "heading block"
    CODE = "code block"
    QUOTE = "quote block"
    UNORDERED_LIST = "unordered list block"
    ORDERED_LIST = "ordered list block"

def block_to_block_type(block):
    lines = block.split("\n")

    if len(lines) == 1:
        line_start = lines[0].split()[0]
        if len(line_start) == line_start.count("#") and len(line_start) <= 6 and len(line_start) >= 1:
            return BlockType.HEADING
    
    if lines[0][:3] == "```" and lines[-1][-3:] == "```":
        return BlockType.CODE
    
    is_quote = True
    is_o_list = True
    is_u_list = True
    count = 1
    for line in lines:
        if not (is_quote or is_o_list or is_u_list):
            break
        if line[0] != ">":
            is_quote = False
        start = line.split()[0]
        if start != "-":
            is_u_list = False
        if start != str(count) + ".":
            is_o_list = False
        count += 1
    
    if is_quote:
        return BlockType.QUOTE
    if is_o_list:
        return BlockType.ORDERED_LIST
    if is_u_list:
        return BlockType.UNORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        block = block.strip()
        if block:
            blocks.append(block)
    return blocks