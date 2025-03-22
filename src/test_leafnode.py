import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_just_tag_and_value(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    

    def test_leaf_to_html_include_url_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p")
            node.to_html()

if __name__ == "__main__":
    unittest.main()