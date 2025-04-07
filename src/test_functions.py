import unittest

from functions import *

class TestFunctions(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = "This is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items"
        blocks = markdown_to_blocks(md)
        result = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(blocks, result)

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        result = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, result)

    def test_split_images(self):
        node = TextNode("some text ![an image](/a-link/) more text [a link](/url/)", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        result = [
            TextNode("some text ", TextType.NORMAL),
            TextNode("an image", TextType.IMAGE, "/a-link/"),
            TextNode(" more text [a link](/url/)", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, result)

    def test_split_links(self):
        node = TextNode("some text ![an image](/a-link/) more text [a link](/url/)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        result = [
            TextNode("some text ![an image](/a-link/) more text ", TextType.NORMAL),
            TextNode("a link", TextType.LINK, "/url/")
        ]
        self.assertEqual(new_nodes, result)

    def test_extract_markdown_images(self):
        text = "some text ![an image](/a-link/) more text [a link](/url/)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("an image", "/a-link/")])

    def test_extract_markdown_links(self):
        text = "some text ![an image](/a-link/) more text [a link](/url/)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("a link", "/url/")])

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
        node = TextNode("This is a text node", TextType.LINK, "/url/")
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"href":"/url/"})

    def test_text_to_html_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "/url/")
        html_node = text_node_to_hmtl_node(node)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"src":"/url/","alt":"This is a text node"})

if __name__ == "__main__":
    unittest.main()