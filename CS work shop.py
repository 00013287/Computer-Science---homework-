

decimal_number = int(input("Enter a decimal number :"))
octal_number = oct(decimal_number).replace("0o", "")
print("The octal value for {} is {}".format(decimal_number,octal_number))