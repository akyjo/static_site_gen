from lib import text_node_to_html_node
from textnode import TextNode, TextType

import unittest


class TestConvertNodes(unittest.TestCase):
    def test_text(self):
        text_n = TextNode("THESE", TextType.NORMAL)
        html_n = text_node_to_html_node(text_n)
        self.assertEqual(html_n.tag, None)
        self.assertEqual(html_n.value, "THESE")

    def test_bold(self):
        text_n = TextNode("THESE", TextType.BOLD)
        html_n = text_node_to_html_node(text_n)
        self.assertEqual(html_n.tag, "b")
        self.assertEqual(html_n.value, "THESE")

    def test_italics(self):
        text_n = TextNode("THESE", TextType.ITALIC)
        html_n = text_node_to_html_node(text_n)
        self.assertEqual(html_n.tag, "i")
        self.assertEqual(html_n.value, "THESE")

    def test_code_tag(self):
        text_n = TextNode("THESE", TextType.CODE)
        html_n = text_node_to_html_node(text_n)
        self.assertEqual(html_n.tag, "code")
        self.assertEqual(html_n.value, "THESE")

    def test_link(self):
        text_n = TextNode("", TextType.LINK, "boot.doot")
        html_n = text_node_to_html_node(text_n)
        self.assertEqual(html_n.tag, "a")
        self.assertEqual(html_n.value, "")
        self.assertEqual(html_n.props, {"href": "boot.doot"})

    def test_img(self):
        text_n = TextNode("desc of img", TextType.IMAGE, url="deez/nuts.jpeg")
        html_n = text_node_to_html_node(text_n)
        self.assertEqual(html_n.tag, "img")
        self.assertEqual(html_n.value, None)
        self.assertEqual(html_n.props, {"src": "deez/nuts.jpeg", "alt": "desc of img"})
