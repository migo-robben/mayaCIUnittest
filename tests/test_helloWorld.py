import unittest
from maya import cmds

from base import MayaBaseTestCase

transform = None
class TestHelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global transform
        transform = cmds.createNode("transform", name="testNode")

    def test_hello_world(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3, "Result Error.")

    def test_node_name(self):
        self.assertEqual(transform, "testNode")

    def test_node_exists(self):
        """Test whether node was actually created."""
        transform_exists = cmds.objExists(transform)
        self.assertTrue(transform_exists)

    def test_visibility_data_type(self):
        """Test whether visibility attribute of node is a boolean."""
        visibility = cmds.getAttr(transform + ".visibility")
        self.assertIs(type(visibility), bool)

    def test_has_roughly_correct_scale(self):
        """Test whether node is roughly at the right scale."""
        transform_scale = cmds.getAttr(transform + ".sx")
        self.assertAlmostEqual(transform_scale, 1.00000001, places=7)

    def test_movement(self):
        """Test whether node can move."""
        target_pos = [1, 2, 3.45]
        cmds.xform(transform, translation=target_pos, worldSpace=True)
        actual_pos = cmds.xform(
            transform, query=True, translation=True, worldSpace=True
        )
        self.assertListEqual(actual_pos, target_pos)

    def test_for_strange_attribute(self):
        """Test for an expected Error."""
        with self.assertRaises(ValueError):
            cmds.getAttr(transform + ".whyWouldItHaveThisAttribute")