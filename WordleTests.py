import unittest
from Wordle import target_word, guess, result

class Testing(unittest.TestCase):

    def test_target_is_a_valid_word(self):
        self.assertTrue(type(target_word) == str)

    def test_target_is_len_5(self):
        self.assertTrue(len(target_word) == 5)

    def test_target_is_letters_only(self):
        self.assertTrue(target_word.isalpha())

    def test_guess_is_word(self):
        self.assertTrue(type(guess) == str)

    def test_guess_is_len_5(self):
        self.assertTrue(len(guess) == 5)

    def test_guess_is_letters_only(self):
        self.assertTrue(guess.isalpha())
    
    def test_at_least_one_letter_wrong(self):
        self.assertTrue("0" in result)

    def test_at_least_one_letter_correct_wrong_place(self):
        self.assertTrue("1" in result)
    
    def test_at_least_one_letter_correct_right_place(self):
        self.assertTrue("2" in result)



if __name__ == '__main__':
    unittest.main()