from textnode import TextNode, TextType


def main():
    type_ = TextType.NORMAL_TEXT
    node = TextNode("dummy text", type_, "localhost:8888")
    print(node)


if __name__ == "__main__":
    main()
