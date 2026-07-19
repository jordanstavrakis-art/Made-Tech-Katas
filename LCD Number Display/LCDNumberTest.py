import unittest
from LCDNumber import lcd_number_display

class Testing(unittest.TestCase):

    def setUp(self):
        pass

    def test_lcd_string_value_exists(self):
        self.assertTrue(type(lcd_number_display) == str)
    def test_lcd_contains_4_line_breaks(self):
        self.assertTrue(lcd_number_display.count("\n") == 4)

if __name__ == '__main__':
    unittest.main()