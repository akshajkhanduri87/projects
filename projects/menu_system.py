# 6/24/25
print("you have 3 options")
print("Type 1 to say hello")
print("Type 2 to add two numbers")
print("Type 3 to quit the program")

user_option = input(("Type your choice here: "))

def add_two_numbers(a,b):
    print(int(a)+int(b))


if user_option == "1":
    print("Hello!")
elif user_option == "2":
    add_two_numbers_option_first_number = (input("Type the first number: "))
    add_two_numbers_option_second_number = (input("Type the second number: "))
    add_two_numbers(add_two_numbers_option_first_number,add_two_numbers_option_second_number)
elif user_option == "3":
    print("You have quit the program")