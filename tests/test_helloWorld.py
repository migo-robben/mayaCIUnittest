import unittest
import maya.cmds as cmds
help(cmds)


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.transform = cmds.createNode("transform", name="testNode")

    def test_hello_world(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3, "Result Error.")

    def test_node_name(self):
        self.assertEqual(self.transform, "testNode")
