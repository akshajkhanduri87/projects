import random
print("Welcome to password checking program!")
print("you have 2 options:")
print("type 1 for generate password and type 2 for validate password")

option = input("type your choice here: ")

def validate_password(password):
    if len(password) < 8 or len(password) > 20:
        return False 

    character_checker = 0   
    for i in range(0,len(password)):
        if password[i] == "@" or password[i] == "#" or password[i] == "!":
            character_checker += 1
            break 
    if character_checker == 0:
        return False 

    uppercase_checker = 0
    for i in range(0,len(password)):
        if password[i].isupper():
            uppercase_checker += 1
            break
    if uppercase_checker == 0:
        return False 

    digit_checker = 0
    for i in range(0,len(password)):
        if password[i].isdigit():
            digit_checker+= 1
            
    if digit_checker < 2:
        return False 

    return True 
        

def generate_password():
    lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Step 1: Randomize size of the password. (8-20 characters)
    # To get all of the lowercase letters, we would have to provide the computer with a list of all the lowercase letters and put it into a string.
    password_length = random.randint(8,21) 
    generated_password = "" 
    for i in range(0,password_length):
        letter = random.choice(lowercase_alphabets)
        generated_password += letter
    return generated_password


if option == "1":
    print("you have selected generate password!")
    print("this is your password")
    password = generate_password()
    print(password)
elif option == "2":
    print("you have selected validate password")
    user_password = input("Please type in what you think your password is: ")
    is_valid = validate_password(user_password)
    if is_valid == True:
        print("This password is valid!")
    else:
        print("The password is invalid")
else:
    print("please input a valid number")

