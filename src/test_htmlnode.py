import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode(
            "h1", 
            "This is the contents of the paragraph", 
            None, 
            {"href": "https://www.google.com","target": "_blank"})
        
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "This is the contents of the paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://www.google.com","target": "_blank"})

    def test_props_to_html(self):
        node = HTMLNode(
            None,
            None,  
            None, 
            {"href": "https://www.google.com","target": "_blank"})
        
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test__repr__(self):
        node = HTMLNode(
            "p",
            "Some more text",
            None,
            {"class": "primary"})

        self.assertEqual(node.__repr__(), "HTMLNode(p, Some more text, children: None, {'class': 'primary'})")

if __name__ == "__main__":
    unittest.main()