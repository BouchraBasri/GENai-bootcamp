# Challenge 1
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)

# Challenge 2
user_input = input("Enter a string: ")

result = ""

for char in user_input:
    if not result or char != result[-1]:
        result += char

print("Result:", result)
