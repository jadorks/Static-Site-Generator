import unittest
from main import extract_title

class TestGenerator(unittest.TestCase):
    def test_extract_title(self):
        markdown = """# Hello World
I am a markdown document"""

        title = extract_title(markdown)

        self.assertEqual(title, "Hello World")

    def test_no_title(self):
        markdown = """I have no title"""

        self.assertRaises(ValueError, extract_title, markdown)


if __name__ == "__main__":
    unittest.main()
