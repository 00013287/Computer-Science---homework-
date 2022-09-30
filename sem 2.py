
def new_line():

    print('*')

# here the function new_line calls one line


def three_lines():

    new_line()

    new_line()

    new_line()

# here the function three_lines calls three lines


def nine_lines():

    three_lines()

    three_lines()

    three_lines()

    print("Printing nine lines")

# here the function nine_lines calls nine lines


def clear_screen():

    nine_lines()

    nine_lines()

    three_lines()

    three_lines()

    new_line()

    print("Total of 25 lines")


clear_screen()

# here clear_screen uses a combination of the functions nine_lines, three_lines, and new_line
# to print a total of twenty-five lines