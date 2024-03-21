import unittest
from osarch import detect_system_os, detect_architecture, detect_system_architecture

class TestOsArch(unittest.TestCase):
    def test_detect_system_os(self):
        self.assertIsInstance(detect_system_os(), str)

    def test_detect_architecture(self):
        # The architecture should also return a string, either "64" or "32".
        self.assertIn(detect_architecture(), ['64', '32'])

    def test_detect_system_architecture(self):
        # This should return a tuple with the OS and architecture.
        result = detect_system_architecture()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], str)
        self.assertIn(result[1], ['64', '32'])

if __name__ == '__main__':
    unittest.main()
