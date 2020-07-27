"""Unittest base class module."""
import os
import sys

import unittest

# Add repository base path to system paths, so Maya can access your scripts.
tests_path = os.path.dirname(os.path.realpath(__file__))
base_path = tests_path.rsplit(os.sep, 1)[0]
if base_path not in sys.path:
    sys.path.insert(0, base_path)

# Initialize Maya - otherwise tests run before Maya is actually ready!
import maya.standalone
maya.standalone.initialize()

from maya import cmds


class MayaBaseTestCase(unittest.TestCase):
    """Base class for all Maya unittests."""

    @classmethod
    def setUpClass(self):
        """Run for every Test-Class, before any method is executed."""
        cmds.file(newFile=True, force=True)

    def tearDown(self):
        """Run after every Test-Class method."""
        cmds.file(newFile=True, force=True)