import re
from htmlnode import LeafNode

from textnode import TextType, TextNode


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


def split_nodes_delim(old_nodes, delimiter, text_type):
    res = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            res.append(node)
            continue
        split = node.text.split(delimiter)
        split_nodes = []
        if len(split) % 2 == 0:
            raise ValueError("Invalid Markdown: unbalanced number of delims!")
        for i in range(len(split)):
            if split[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(split[i], text_type))
        res.extend(split_nodes)
    return res


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_md_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_md_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes


def extract_md_images(text: str) -> list[(str,)]:
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    res = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return res


def extract_md_links(text: str) -> list[(str,)]:
    # "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    res = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return res


def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.NORMAL)
    nodes = split_nodes_delim([node], "**", TextType.BOLD)
    nodes = split_nodes_delim(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delim(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes
