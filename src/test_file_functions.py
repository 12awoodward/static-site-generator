import unittest

from main import *

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md = "# heading\n\nsome text"
        self.assertEqual(extract_title(md), "heading")
    
    def test_extract_title_error(self):
        md = "## sub-heading\n\nother text"
        self.assertRaises(Exception, extract_title, md)

if __name__ == "__main__":
    unittest.main()