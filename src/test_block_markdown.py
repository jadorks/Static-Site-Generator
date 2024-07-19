import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_quote,
    block_type_unordered_list,
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"

        blocks = markdown_to_blocks(markdown)

        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocks,
        )

    def test_empty_markdown_to_blocks(self):
        markdown = ""

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(len(blocks), 0)

    def test_heading_type(self):
        block = "# Hello this is a heading"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_heading)

    def test_paragraph_type(self):
        block = "Hello I am a paragraph"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_code_type(self):
        block = "```\nprint()\n```"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_code)

    def test_ordered_list(self):
        block = "1. Hello\n2. I am\n3. A list"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_ordered_list)

    def test_invalid_ordered_list(self):
        block = "1. Hello\nI am not valid"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_unordered_list_asterisk(self):
        block = "* Hello\n* I do not like order"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_unordered_list)

    def test_unordered_list_dash(self):
        block = "- Hello\n- I do not like order"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_unordered_list)

    def test_invalid_unordered_list_asterisk(self):
        block = "* Hello\nI am not valid"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_invalid_unordered_list_dash(self):
        block = "- Hello\nI am not valid"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_quote(self):
        block = "> Hello\n> A wise man once said\n> You are a quote"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_quote)

    def test_invalid_quote(self):
        block = "> Hello\nA wise man once said\nYou are not a quote"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, block_type_paragraph)


if __name__ == "__main__":
    unittest.main()
