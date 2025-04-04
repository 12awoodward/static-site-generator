import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p", [
            LeafNode(None, "Normal Text"),
            LeafNode("b", "Bold Text"),
            LeafNode(None, "Normal Text")
        ], {"a":"b"})
        txt = '<p a="b">Normal Text<b>Bold Text</b>Normal Text</p>'
        self.assertEqual(node.to_html(), txt)

    def test_to_html2(self):
        inner = LeafNode("b", "grandchild")
        mid = ParentNode("span", [inner])
        outer = ParentNode("div", [mid])
        txt = '<div><span><b>grandchild</b></span></div>'
        self.assertEqual(outer.to_html(), txt)

    def test_to_html_valueerror(self):
        node = ParentNode("b", [])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_valueerror2(self):
        node = ParentNode(None, [LeafNode(None,"text")])
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()