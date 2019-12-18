import unittest
from CreditCardValidator import CreditCardValidator

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.sut = CreditCardValidator()
                
    def test_valid(self):
        self.assertTrue(self.sut.execute("4123456789123456"))
        self.assertTrue(self.sut.execute("5123-4567-8912-3456"))
        self.assertTrue(self.sut.execute("4123356789123456"))
    
    def test_invalid_repeating_digits(self):
        self.assertFalse(self.sut.execute("4424444424442444"))
        self.assertFalse(self.sut.execute("5133-3367-8912-3456"))
    
    def test_invalid_bad_seperators(self):
        self.assertFalse(self.sut.execute("5122-2368-7954 - 3214"))
        self.assertFalse(self.sut.execute("5123 - 3567 - 8912 - 3456"))
        self.assertFalse(self.sut.execute("5123_3567_8912_3456"))

    def test_invalid_bad_separator_groups(self):
        self.assertFalse(self.sut.execute("61234-567-8912-3456"))
    
    def test_invalid_non_numeric_digits(self):
        self.assertFalse(self.sut.execute("44244x4424442444"))
        
    def test_invalid_start_character(self):
        self.assertFalse(self.sut.execute("0525362587961578"))
        
    
if __name__ == '__main__':
    unittest.main()