import unittest

from textnode import (TextNode, text_type_text, text_type_italic, text_type_bold)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_text_type_neq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", text_type_text, "https://google.com")
        node2 = TextNode("This is a text node", text_type_text, "https://google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "https://google.com")
        self.assertEqual("TextNode(This is a text node, bold, https://google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()