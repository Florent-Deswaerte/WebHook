import unittest

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5 + 5, 10, "Erreur: 5 + 5 n'est pas égal à 10")

if __name__ == "__main__":
    unittest.main()