"""
write a program that displays LCD style numbers.
"""
class zero:
    top = " _ "
    middle = "| |"
    bottom = "|_|"

class one:
    top = "   "
    middle = " | "
    bottom = " | "

class two:
    top = " _ "
    middle = " _|"
    bottom = "|_ "

class three:
    top = " _ "
    middle = " _|"
    bottom = " _|"

class four:
    top = "   "
    middle = "|_|"
    bottom = "  |"

class five:
    top = " _ "
    middle = "|_ "
    bottom = " _|"

class six:
    top = " _ "
    middle = "|_ "
    bottom = "|_|"

class seven:
    top = " _ "
    middle = "  |"
    bottom = "  |"

class eight:
    top = " _ "
    middle = "|_|"
    bottom = "|_|"

class nine:
    top = " _ "
    middle = "|_|"
    bottom = " _|"

numbers_dict = {'0': zero,
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine}

def print_LCD(list):
    sections = ["top","middle","bottom"]
    lcd_output = ""
    for s in sections:
        if s != "top":
            lcd_output += "\n"
        for n in list:
            if n in numbers_dict.keys():
                lcd_output += getattr(numbers_dict[n],s)
            else:
                pass
    print(lcd_output)


number_input = list(input("Enter some numbers: "))
print_LCD(number_input)