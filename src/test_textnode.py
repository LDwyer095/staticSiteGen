import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eqLINK(self):
        node = TextNode("This is a text node", TextType.LINK, "www.test.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.test.com")
        self.assertEqual(node, node2)
    
    def test_difLINK(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_difTEXT(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is dif text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_difTextType(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))

if __name__ == "__main__":
    unittest.main()