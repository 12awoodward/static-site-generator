import unittest

from markdown_to_html import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = "This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with _italic_ text and `code` here"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_headings(self):
        md = "# This is h1 heading\n\n### h3 heading\n\n###### This is another heading with _italic_ text and `code` here"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is h1 heading</h1><h3>h3 heading</h3><h6>This is another heading with <i>italic</i> text and <code>code</code> here</h6></div>",
        )

    def test_codeblock(self):
        md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quotes(self):
        md = "> This is a quote that _should_ show\n> the **inline** stuff"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that <i>should</i> show the <b>inline</b> stuff</blockquote></div>",
        )

    def test_u_list(self):
        md = "- This is an **unordered**\n- list in a ul tag\n- with _italic_ text and `code` here"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an <b>unordered</b></li><li>list in a ul tag</li><li>with <i>italic</i> text and <code>code</code> here</li></ul></div>",
        )

    def test_o_list(self):
        md = "1. This is an **ordered**\n2. list in a ol tag\n3. with _italic_ text and `code` here"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an <b>ordered</b></li><li>list in a ol tag</li><li>with <i>italic</i> text and <code>code</code> here</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()