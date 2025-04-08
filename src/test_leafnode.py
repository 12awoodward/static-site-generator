import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p","text")
        txt = '<p>text</p>'
        self.assertEqual(node.to_html(), txt)
    
    def test_to_html2(self):
        node = LeafNode(None,"text")
        txt = 'text'
        self.assertEqual(node.to_html(), txt)

    def test_to_html3(self):
        node = LeafNode("a","text", {"href":"/link/"})
        txt = '<a href="/link/">text</a>'
        self.assertEqual(node.to_html(), txt)

        

if __name__ == "__main__":
    unittest.main()