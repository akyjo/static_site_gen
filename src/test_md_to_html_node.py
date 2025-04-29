import unittest

from lib import markdown_to_html_node


class TestMDToHtml(unittest.TestCase):
    def test_md_para(self):
        md = """
        This is para, bla bla
        """
        valid_html = "<div><p>This is para, bla bla</p></div>"

        self.assertEqual(markdown_to_html_node(md).to_html(), valid_html)
