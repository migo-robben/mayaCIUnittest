import unittest


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3, "Result Error.")