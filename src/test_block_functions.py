import unittest

from block_functions import *

class TestBlockFunctions(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        block = "some text\nin a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        block = "### h3 heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```code\nin a\nblock```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "```code in one line```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = ">quote\n>block"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_u_list(self):
        block = "- items\n- in\n- a\n- list"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_o_list(self):
        block = "1. items\n2. in\n3. order"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_markdown_to_blocks(self):
        md = "This is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items"
        blocks = markdown_to_blocks(md)
        result = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(blocks, result)

if __name__ == "__main__":
    unittest.main()