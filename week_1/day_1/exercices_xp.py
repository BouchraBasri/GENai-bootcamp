# Exercice 1
print("Hello world\n" * 4)

# Exercice 2
result = (99**3) * 8
print(result)

# Exercice 3
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
print('"3" > 3:', "3" > 3 ) #Error
print("Hello" == "hello") #False

# Exercice 4
computer_brand = "hp"
print("I have an ", computer_brand, " computer.")

# Exercice 5
name = "Bouchra"
age = 23
shoe_size = 37
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)

# Exercice 6
a = 23
b = 61
if a > b:
    print("Hello world")

# Exercice 7
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
# Exercice 8
user_name = input("What's your name?")
name = "Bouchra"
if user_name == name:
    print("We have the same name.")
else:
    print("Nice to meet you!")

# Exercice 9
height = int(input("What's your height?(cm)"))
min_height = 145
if min_height <= height:
    print("You're tall enough to ride.")
else:
    print("you need to grow some more to ride.")

             