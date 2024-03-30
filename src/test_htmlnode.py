import unittest

from htmlnode import HTMLNode


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