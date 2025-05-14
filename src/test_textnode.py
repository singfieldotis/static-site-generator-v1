import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is another text node", TextType.TEXT)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node6 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node7 = TextNode("This is a text node", TextType.CODE, "https://www.boot.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node5, node7)


if __name__ == "__main__":
    unittest.main()