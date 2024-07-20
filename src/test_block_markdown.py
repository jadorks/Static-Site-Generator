import unittest
from block_markdown import (
    markdown_to_blocks,
    markdown_to_html_node,
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

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )



if __name__ == "__main__":
    unittest.main()
