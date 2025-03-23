from htmlnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node: TextType) -> LeafNode:
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": f"{text_node.url}"})
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.IMAGE:
            return LeafNode(
                "img",
                None,
                props={"src": f"{text_node.url}", "alt": f"{text_node.text}"},
            )
        case _:
            raise Exception("Invalid TextType")
