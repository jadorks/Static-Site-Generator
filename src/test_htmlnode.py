import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html(self):
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

    def test_parent_to_html(self):
        parentNode = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            parentNode.to_html(),
        )

    def test_nested_parents(self):
        parentNode = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("p", "Hello world!"),
                        LeafNode(
                            "a",
                            "I am a link",
                            {"href": "https://google.com", "target": "_blank"},
                        ),
                        ParentNode("div", [LeafNode("p", "Im so deep bro!")]),
                    ],
                ),
                LeafNode(None, "Raw Text, LFG!!"),
            ],
        )

        self.assertEqual(
            '<div><div><p>Hello world!</p><a href="https://google.com" target="_blank">I am a link</a><div><p>Im so deep bro!</p></div></div>Raw Text, LFG!!</div>',
            parentNode.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
