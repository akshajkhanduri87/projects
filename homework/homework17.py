# Homework: Create a function that counts how many times a letter appears in a word
#
# Your function should:
# - Take a word and a letter as input
# - Use a for loop to go through each character in the word
# - Use an if statement to check if the character matches the letter
# - Count how many times the letter appears
# - Return the count
#
# Example:
# Input: word = "banana", letter = "a"
# Output: 3 (because 'a' appears 3 times in "banana")

#def count_letter(word, letter):
    # Your code here

# Homework: Create a function that adds up all even numbers in a list
#
# Your function should:
# - Take a list of numbers as input
# - Use a for loop to go through each number
# - Use an if statement to check if the number is even
# - Add up all the even numbers
# - Return the total
#
# Example:
# Input: [1, 2, 3, 4, 5, 6]
# Output: 12 (because 2 + 4 + 6 = 12)

def sum_even_numbers(numbers):
    total = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total


