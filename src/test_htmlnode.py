import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "h1",
            "I love programming",
            None,
            {"style": "border: solid 1px red; color: red"},
        )

        node2 = HTMLNode(
            "a",
            "I love programming",
            None,
            {"href": "https://google.com", "target": "_blank"},
        )

        node3 = HTMLNode("p", "Hello world")

        attrs = node.props_to_html()
        attrs2 = node2.props_to_html()
        attrs3 = node3.props_to_html()

        self.assertEqual(' style="border: solid 1px red; color: red"', attrs)
        self.assertEqual(' href="https://google.com" target="_blank"', attrs2)
        self.assertEqual("", attrs3)

    def test_to_html(self):
        leafNode = LeafNode(
            "p", "Hello World!", {"style": "border: solid 1px red; color: red"}
        )
        leafNode2 = LeafNode("p", "I have no attrs")
        leafNode3 = LeafNode(None, "I am a raw node", None)

        self.assertEqual(
            '<p style="border: solid 1px red; color: red">Hello World!</p>',
            leafNode.to_html(),
        )
        self.assertEqual(
            "<p>I have no attrs</p>",
            leafNode2.to_html(),
        )
        self.assertEqual("I am a raw node", leafNode3.to_html())


if __name__ == "__main__":
    unittest.main()
