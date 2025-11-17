# Exercice 1
list1 = [1, 2, 3]
list2 = [11, 12, 13]

list1.extend(list2)

print(list1)

# Exercice 2
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

# Exercice 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name please: ")

if user_name in names:
    print("Index: ", names.index(user_name))
else:
    print("Name not found")

# Exercice 4
num_1 = float(input("Input the 1st number: "))
num_2 = float(input("Input the 2nd number: "))
num_3 = float(input("Input the 3rd number: "))

greatest = max(num_1, num_2, num_3)

print("The greatest number is:", greatest)

# Exercice 5
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")

# Exercice 6
words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

letter = input("Enter a single letter: ")

print("\nResults:")
for word in words:
    if letter in word:
        print(f"In '{word}', the letter '{letter}' first appears at index {word.index(letter)}.")
    else:
        print(f"The letter '{letter}' doesn't appear in the word '{word}'.")
# Exercice 7
numbers = list(range(1, 1000001))

print("Minimum number is: ", min(numbers))
print("Maximum number is: ", max(numbers))

print("Sum of all numbers in the list is: ", sum(numbers))

# Exercice 8
numbers = input("Enter a comma-separated numbers: ")

list_numbers = numbers.split(",")
tuple_numbers = tuple(list_numbers)

print(list_numbers)
print(tuple_numbers)
# Exercice 9
import random

wins = 0
losses = 0

while True:
    user_input = input("Enter a number from 1 to 9 (or type 'quit' to quit): ")

    if user_input.lower() == 'q':
        break

    if not user_input.isdigit():
        print("Please enter a valid number!")
        continue
    
    user_number = int(user_input)

    if user_number < 1 or user_number > 9:
        print("Number must be between 1 adn 9! ")
        continue

    random_number = random.randint(1, 9)

    if user_number == random_number:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time.")
        losses += 1

print("\nGame over!")
print("Total Wins: ", wins)
print("Total Losses: ", losses)
