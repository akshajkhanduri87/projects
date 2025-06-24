print("Welcome to the Leap Year checker!")
print("This program tells you if the year entered is leap or regualar year")
print("Please only enter numerical values")

option = int(input("Enter the year you want to validate "))

# We convert the variable option into an integer format because we are entering a numerical value, not a string value.
# The function helps the program figure out what to do if the year is leap or not. In this case, it is to print.
# We then call the function and tell and give it the variable option because the numerical value entered by the user is being checked.

def is_leap_year(year):
    if (year % 4 ==0):
        print("This is a leap year and has 52 weekends")
    else:
        print("This is a regular year and has 52 weekends")

    

is_leap_year(option)

    


