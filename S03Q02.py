"""Ask the user to enter a number.
- If the number is a single digit number,
     add 7 to it, and print the number in its unit’s place
- If the number is a two digit number,
    raise the number to the power of 5, 
    and print the number in its unit’s place
- If the number is a three digit number, 
    ask the user to enter another number. 
    Add the 2 numbers and print the number in its unit’s place

Use the solution provided in S03Q01 as the template for this exercises.
- Instead of doing a print to print the final result in "perform_check" function 
call separate functions : 
   do_1digit_oper() and
   do_2digit_oper() and
   do_3digit_oper()
that will perform the required operations based on the number of digits.
"""

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
    if number < 10:
        result = do_1digit_oper(number)
    elif 10 <= number < 100:
        result = do_2digit_oper(number)
    elif 100 <= number < 1000:
        result = do_3digit_oper(number)
    else:
        result = "number is not within range"
    print("Unit's place of result:", result)
    
def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    value = int(input("Enter the number: "))
    return value

def do_1digit_oper(number):
    val = number + 7
    return = val % 10

def do_2digit_oper(number):
    val = number ** 5
    return = val % 10

def do_3digit_oper(number):
    another = int(input("Enter another number: "))
    val = number + another
    return val % 10


# Main starts from here
num1 = get_number()
perform_check(num1)



"""

def perform_check(number):
    """ This function uses helper functions
        to perform the required operations
        based on the number of digits.
    """
    if number < 10:
        result = do_1digit_oper(number)
    elif 10 <= number < 100:
        result = do_2digit_oper(number)
    elif 100 <= number < 1000:
        result = do_3digit_oper(number)
    else:
        result = "Number is not within the expected range (1-999)"
    
    print("Unit's place of result:", result)


def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    value = int(input("Enter the number: "))
    return value


def do_1digit_oper(number):
    val = number + 7
    return val % 10


def do_2digit_oper(number):
    val = number ** 5
    return val % 10


def do_3digit_oper(number):
    another = int(input("Enter another number: "))
    val = number + another
    return val % 10


# Main starts from here
num1 = get_number()
perform_check(num1)

"""
