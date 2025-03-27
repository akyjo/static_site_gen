from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md: str) -> BlockType:
    # TODO, return appropriate part of block, since we already do processing with splitting
    block_words = md.split(" ")
    md_newlines = md.split("\n")
    hash_ct = block_words[0].count("#")

    if hash_ct < 7 and hash_ct > 0:
        return BlockType.HEADING

    if block_words[0] == "```" and block_words[-1] == "```":
        return BlockType.CODE

    quote_check = [True if x[0] == ">" else False for x in md_newlines]
    if all(quote_check):
        return BlockType.QUOTE

    uol_check = [True if x[0] == "-" else False for x in md_newlines]
    if all(uol_check):
        return BlockType.UNORDERED_LIST

    ol_check = [
        int(x.split(".")[0]) if x.split(".")[0].isnumeric() else 0
        for x in list(filter(lambda x: "." in x, md_newlines))
    ]
    if sum(ol_check) == sum(range(1, len(md_newlines) + 1)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
