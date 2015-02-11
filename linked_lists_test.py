import unittest
from LinkedList import *

class TestNode(unittest.TestCase):
    """
    Test suite for Node related functions.
    """

    def test_init(self):
        """
        Tests if a node was made properly
        """
        self.new_node = LLNode(6)
        self.assertEqual(print(self.new_node), "Value is: 6")
