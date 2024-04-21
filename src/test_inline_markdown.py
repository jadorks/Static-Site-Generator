import unittest
from inline_markdown import split_nodes_delimiter

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("I love **chocolate** milk", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("I love ", text_type_text),
                TextNode("chocolate", text_type_bold),
                TextNode(" milk", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("I love *chocolate* milk", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("I love ", text_type_text),
                TextNode("chocolate", text_type_italic),
                TextNode(" milk", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("I love `chocolate` milk", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("I love ", text_type_text),
                TextNode("chocolate", text_type_code),
                TextNode(" milk", text_type_text),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
