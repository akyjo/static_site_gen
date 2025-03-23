import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        html_node = HTMLNode(tag="a", value="b", props={"a": "aval", "b": "bval"})
        self.assertEqual(
            html_node.__repr__(),
            "HTMLNode: {'tag': 'a', 'value': 'b', 'children': None, 'props': {'a': 'aval', 'b': 'bval'}}",
        )

    def test_props_to_html(self):
        html_node = HTMLNode(tag="a", value="b", props={"a": "aval", "b": "bval"})
        out = html_node.props_to_html()
        self.assertEqual(out, ' a="aval" b="bval"', "needs a space infront ")

    def test_to_html(self):
        html_node = HTMLNode(tag="a", value="b", props={"a": "aval", "b": "bval"})
        self.assertRaises(NotImplementedError, html_node.to_html)

    def test_leaf_node(self):
        leaf = LeafNode("p", "Hello")
        self.assertEqual(leaf.to_html(), "<p>Hello</p>")

    def test_leaf_node_no_tag(self):
        leaf = LeafNode(None, "Hello")
        self.assertEqual(leaf.to_html(), "Hello")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_gg(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("i", "grandchild2")
        child_node = ParentNode(
            "span", [grandchild_node, grandchild_node2], props={"je": "bait"}
        )
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            '<div><span je="bait"><b>grandchild</b><i>grandchild2</i></span></div>',
        )
