# tests/test_simple.py

import unittest

class SimpleTest(unittest.TestCase):
    def test_always_true(self):
        """A simple test that always passes."""
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
