import unittest

from block import block_to_block_type, BlockType


class TestBlock(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "###### bla bla "
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type2(self):
        block = "``` bla \nbla ```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type3(self):
        block = "> bla\n> bla bla\n>bla"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type4(self):
        block = "- bla\n- bla bla\n-bla"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type5(self):
        block = "1. bla\n2. bla bla\n3. bla"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type6(self):
        block = "regular ordinary paragraph. Dude. Don't ask me where I'm going, I'm going insane."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
