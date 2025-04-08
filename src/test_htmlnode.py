import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode()
        txt = "HMTLNode(tag=None|props=None|value=None|children=None)"
        self.assertEqual(str(node), txt)

    def test_repr2(self):
        node = HTMLNode("p", "Some Text", None, {"href":"/page/"})
        node2 = HTMLNode(props={"href":"/page/"}, tag="p", value="Some Text")
        self.assertEqual(str(node), str(node2))

    def test_repr3(self):
        node = HTMLNode(children=[HTMLNode()])
        txt = "HMTLNode(tag=None|props=None|value=None|children=[HMTLNode(tag=None|props=None|value=None|children=None)])"
        self.assertEqual(str(node), txt)

    def test_props_to_html(self):
        node = HTMLNode(props={"a":"value","href":"/link/"})
        txt = ' a="value" href="/link/"'
        self.assertEqual(node.props_to_html(), txt)
        

if __name__ == "__main__":
    unittest.main()