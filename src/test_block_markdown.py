import unittest
from block_markdown import markdown_to_blocks


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

        


if __name__ == "__main__":
    unittest.main()
