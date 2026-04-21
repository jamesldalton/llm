import unittest
from src.token import tokenizer

class TestTokenizer(unittest.TestCase):
    def test_tokenizer(self):
        self.assertEqual(tokenizer("A"), [34])
        self.assertEqual(tokenizer("Hi"), [41, 74])
        self.assertEqual(tokenizer(""), [])