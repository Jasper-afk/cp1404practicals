"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

ValueError will occur when getting user input for numerator and denominator
if anything other than an integer is entered.

2. When will a ZeroDivisionError occur?

ZeroDivisionError will occur when the program attempts divide the numerator by the denominator
and a 0 is entered by the user for one of the inputs.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Yes I can.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero, enter a number greater than zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
