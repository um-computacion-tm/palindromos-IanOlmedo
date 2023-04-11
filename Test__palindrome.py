import unittest
from palindrome import palindromex

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple_true(self):
        self.assertEqual(palindromex("aba"), True)
        
    def test_palindrome_simple_false(self):
        self.assertEqual(palindromex("abc"), False)
        
    def test_palindrome_empty_string(self):
        self.assertEqual(palindromex(""), True)
        
    def test_palindrome_single_letter(self):
        self.assertEqual(palindromex("a"), True)
        
    def test_palindrome_different_case(self):
        self.assertEqual(palindromex("Racecar"), True)
        self.assertEqual(palindromex("Python"), False)

        if __name__=="__main__":
            unittest.main()