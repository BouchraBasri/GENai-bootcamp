# Exercice 1
import math

C = 50
H = 30

user_input = input("Enter a comma-separated numbers: ")

D_values = user_input.split(",")

result = []

for d in D_values:
    D = float(d)
    Q = math.sqrt((2 * C * D) / H)
    result.append(str(int(Q)))

print(",".join(result))

# Exercice 2
import random

numbers = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]

print("Numbers: ", numbers)
print("Numbers in descending order: ", sorted(numbers, reverse=True))
print("The sum of all the numbers is: ", sum(numbers))

first_last = [numbers[0], numbers[-1]]
print("First & last numbers: ", first_last)

greater_than_50 = []
for n in numbers:
    if n > 50:
        greater_than_50.append(n)
print("The numbers greater than 50 are: ", greater_than_50)

smaller_than_10 = []
for n in numbers:
    if n < 10:
        smaller_than_10.append(n)
print("The numbers smaller than 10 are: ", smaller_than_10)

squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

unique_numbers = list(set(numbers))
print(unique_numbers)
print("Count of unique numbers:", len(unique_numbers))

avg = sum(numbers) / len(numbers)
print("Average of the all numbers is: ", avg)

print("The greatest number is: ", max(numbers))

print("The smallest numbers is: ", min(numbers))

manual_sum = 0
manual_max = numbers[0]
manual_min = numbers[0]
count = 0
for n in numbers:
    manual_sum += n

    if n > manual_max:
        manual_max = n
    
    if n < manual_min:
        manual_min = n
    
    count += 1

manual_avg = manual_sum / count

print("Manual sum: ", manual_sum)
print("Manual max: ", manual_max)
print("Manual min: ", manual_min)
print("Manual average: ", manual_avg)

user_numbers = []
for n in range(10):
    user_input = int(input("Enter an integer between -100 and 100: "))
    user_numbers.append(user_input)

print("Your list: ", numbers)

random_numbers = []
for n in range(10):
    random_input = random.randint(-100, 100)
    random_numbers.append(random_input)

print("Random numbers list: ", random_numbers)

random_above_50 = []
for n in range(10):
    random_50 = random.randint(50, 100)
    random_above_50.append(random_50)

print("Random numbers greater than 50: ", random_above_50)

#The code will still work even if the number of random numbers is not equal to 10 
#because none of the opertions depend on the list having a specific length.

# Exercice 3
import string

paragraph = """Artificial intelligence is transforming the world.
It helps doctors diagnose diseases, supports engineers in solving complex problems,
and allows businesses to understand their customers better.
Ai continues to evolve every day."""

print(paragraph)

num_characters = len(paragraph)
print(f"The paragraph contains {num_characters}  character.")

sentences = paragraph.split(".")
sentences = [s.strip() for s in sentences if s.strip() != ""]
num_sentences = len(sentences)
print("Number of sentences in the paragraph is: ", num_sentences)

clean_text = paragraph.translate(str.maketrans("", "", string.punctuation))
words = clean_text.split()
num_words = len(words)
print(f"The paragraph contains {num_words} words.")

unique_words = set(word.lower() for word in words)
num_unique_words = len(unique_words)
print("Number of unique words in the paragraph is: ", num_unique_words)

non_whitespace = len([c for c in paragraph if not c.isspace()])
print("Number of non whitespace is: ", non_whitespace)

avg_words_per_sentence = num_words / num_sentences
print("The average of the words per sentence is: ",avg_words_per_sentence)

num_non_unique = num_words - num_unique_words
print("The number of nonn unique words is: ", num_non_unique)

# Exercice 4
text = input("Enter a sentence: ")

words = text.split()

frequency = {}

for w in words:
    if w in frequency:
        frequency[w] += 1
    else:
        frequency[w] = 1

for word in sorted(frequency):
    print(f"{word}:{frequency[word]}")