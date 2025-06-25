# 6/24/25
import random
print("You have to guess a number between 1 and 10")
print("You have 3 chances to guess the number")
user_guess = int(input("Enter your first guess: "))
def function_feedback(user_guess):
    actual_number = random.randint(1,10)
    if user_guess > actual_number:
        print("Too high!")
        secondguess = int(input("Guess again: "))
        if secondguess < actual_number:
            print("Too low!")
            third_guess = int(input("Guess again: "))
            if third_guess > actual_number:
                print("The number was:", actual_number)
            elif third_guess < actual_number:
                print("The number was:", actual_number)
            else:
                print("Correct!")
        elif secondguess > actual_number:
            print("Too high!")
            third_guess = int(input("Guess again: "))
            if third_guess > actual_number:
                print("The number was:", actual_number)
            elif third_guess < actual_number:
                print("The number was:", actual_number)
            else:
                print("Correct!")
        else:
            print("Correct!")
    elif user_guess < actual_number:
        print("Too low!")
        secondguess = int(input("Guess again: "))
        if secondguess < actual_number:
            print("Too low!")
            third_guess = int(input("Guess again: "))
            if third_guess > actual_number:
                print("The number was:", actual_number)
            elif third_guess < actual_number:
                print("The number was:", actual_number)
            else:
                print("Correct!")
        elif secondguess > actual_number:
            print("Too high")
            third_guess = int(input("Guess again "))
            if third_guess > actual_number:
                print("The number was:", actual_number)
            elif third_guess < actual_number:
                print("The number was:", actual_number)
            else:
                print("Correct!")
        else:
            print("Correct!")
    else:
        print("Correct!")
    

function_feedback(user_guess)