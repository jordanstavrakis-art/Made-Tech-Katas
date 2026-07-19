"""
write a program that displays LCD style numbers.
"""
class zero:
    top = " _ "
    extra_top = "| |"
    middle = "| |"
    extra_bottom = "| |"
    bottom = "|_|"

class one:
    top = "   "
    extra_top = " | "
    middle = " | "
    extra_bottom = " | "
    bottom = " | "

class two:
    top = " _ "
    extra_top = "  |"
    middle = " _|"
    extra_bottom = "|  "
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
                '2': two}
                # '3': three,
                # '4': four,
                # '5': five,
                # '6': six,
                # '7': seven,
                # '8': eight,
                # '9': nine}

def print_LCD(list,height=1,width=1):
    lcd_output = ""
    # Check if additonal height needed. If not ignore extra height sections
    if height == 1:
        sections = ["top","middle","bottom"]
    else:
        sections = ["top","extra_top","middle","extra_bottom","bottom"]
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
# height_input = list(input("Enter value for height: "))
# width_input = list(input("Enter value for width: "))
print_LCD(number_input)