import unittest

from functions import *

class TestFunctions(unittest.TestCase):
    def test_split_nodes_bold(self):
        node = TextNode("Some **bold** text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, result)

    def test_split_nodes_italic(self):
        node = TextNode("Some _italic_ text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        result = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, result)

    def test_split_nodes_code(self):
        node = TextNode("Some `code` text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, result)

    def test_split_nodes_error(self):
        node = TextNode("some _text", TextType.NORMAL)
        self.assertRaises(Exception, split_nodes_delimiter, node, "_", TextType.ITALIC)

    def test_text_to_html_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_to_html_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_to_html_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_to_html_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_to_html_link(self):
        node = TextNode("[This is a text node](/url/)", TextType.LINK)
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"href":"/url/"})

    def test_text_to_html_image(self):
        node = TextNode("![This is a text node](/url/)", TextType.IMAGE)
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"src":"/url/","alt":"This is a text node"})

if __name__ == "__main__":
    unittest.main()