import unittest

from textnode import TextNode, TextType
from lib import split_nodes_delim


class TestSplitNodesDelim(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delim([node], "`", TextType.CODE)
        should_be = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]

        self.assertEqual(new_nodes, should_be)

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.NORMAL)
        new_nodes = split_nodes_delim([node], "**", TextType.BOLD)
        should_be = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
        ]

        self.assertEqual(new_nodes, should_be)

    def test_italics(self):
        node = TextNode("This is text with a __italics__ word", TextType.NORMAL)
        new_nodes = split_nodes_delim([node], "__", TextType.ITALIC)
        should_be = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italics", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ]

        self.assertEqual(new_nodes, should_be)

    def test_bold_and_italics(self):
        node = TextNode(
            "This is text with a **bold** word and __italic__ word", TextType.NORMAL
        )
        new_nodes = split_nodes_delim([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delim(new_nodes, "__", TextType.ITALIC)
        should_be = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertListEqual(new_nodes, should_be)

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delim([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
