import unittest
import re
from LCDNumber import zero

class Testing(unittest.TestCase):
    valid_characters = r"[|_ ]+"
    zero_top = getattr(zero,"top")
    zero_extra_top = getattr(zero,"extra_top")
    zero_middle = getattr(zero,"middle")
    zero_extra_bottom = getattr(zero,"extra_bottom")
    zero_bottom = getattr(zero,"bottom")

    # def test_lcd_is_3_lines_high(self):
    #     self.assertIn(getattr(zero,"top"),zero)
    #     self.assertIn(getattr(zero,"top"),zero)
    #     self.assertIn(getattr(zero,"top"),zero)

    def test_lcd_only_contains_correct_characters(self):
            self.assertTrue(re.fullmatch(self.valid_characters,str(self.zero_top)))
            self.assertTrue(re.fullmatch(self.valid_characters,str(self.zero_middle)))
            self.assertTrue(re.fullmatch(self.valid_characters,str(self.zero_bottom)))

    # def test_zero_output_correct(self):
    #     self.assertTrue(zero.top == " _ ")
    #     self.assertTrue(zero.middle == "| |")
    #     self.assertTrue(zero.bottom == "|_|")
    
    def test_zero_width_2(self):
         expected_top = " __ "
         expected_middle = "|  |"
         expected_bottom = "|__|"
         self.assertTrue(self.zero_top == expected_top)
         self.assertTrue(self.zero_middle == expected_middle)
         self.assertTrue(self.zero_bottom == expected_bottom)
    
    def test_zero_can_do_height_2(self):
         expected_extra_top = "|  |"
         expected_extra_bottom = "|  |"
         self.assertTrue(self.zero_extra_top == expected_extra_top)
         self.assertTrue(self.zero_extra_bottom == expected_extra_bottom)

         


if __name__ == '__main__':
    unittest.main()