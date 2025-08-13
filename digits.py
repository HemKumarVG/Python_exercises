""" What does this program do ?
Take 2 numbers from the user. Print which number is a 2 digit number, 
and which number is a 3 digit number. If it is neither, then print the number as it is
"""
# Implement the helper functions here

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    # Your solution code goes here
    # Invoke check_if_2digit and
    # check_if_3digit to check if the number
    # matches the criteria and print accordingly
    if 9 < number < 100:
        print("The number is 2 digit")
    elif 99 < number < 1000:
        print("The number is 3 digit")
    else:
        print("number")
    
def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    value = int(input("Enter the number: "))
    return value

# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
