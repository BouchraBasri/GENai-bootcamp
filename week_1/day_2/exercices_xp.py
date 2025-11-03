# Exercice 1
my_favorite_numbers = {3, 6, 9}

my_favorite_numbers.add(12)
my_favorite_numbers.add(15)

print("After adding: ", my_favorite_numbers)

my_favorite_numbers.remove(15)

print("After removing the last number: ", my_favorite_numbers)

friend_favorite_numbers = {4, 10, 18, 20}

our_favorite_numbers = my_favorite_numbers.union(friend_favorite_numbers)

print("Our favorite numbers: ", our_favorite_numbers)

# Exercice 2
my_tuple = (1, 2, 3, 4)
print("Original tuple:", my_tuple)

my_tuple.append(5) #Error


# Exercice 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")
basket.insert(0, "Apples")

apple_count = basket.count("Apples")
print("Number of 'Apples' in the list:", apple_count)

basket.clear()

print("Final list:", basket)

# Exercice 4
numbers = []

for i in range(3, 11):
    numbers.append(i / 2)

print(numbers)

# Exercice 5
for number in range(1, 21):
    print(number)

for numbers in range(1, 21):
    if number % 2 == 0:
        print(number)

# Exercice 6
name = input("Please enter your name: ")

while True:

    if name.isdigit() or len(name) < 3:
        name = input("Give the correct name: ")
    else:
        print("Thank you!")
        break

# Exercice 7
favorite_fruits = input("Enter your favorite fruits (separated by spaces): ")

favorite_fruits_list = favorite_fruits.split()

chosen_fruit = input("Enter the name of a fruit: ")

if chosen_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercice 8
toppings = []
base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").lower()
    
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

total_price = base_price + (len(toppings) * topping_price)

print("\nYour pizza toppings are:", ", ".join(toppings))
print(f"Total price: ${total_price:.2f}")

# Exercice 9
total_price = 0

while True:
    age_input = input("Enter the age of a family member (or type 'done' to finish): ").lower()

    if age_input == "done":
        break

    age = int(age_input)

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_price += ticket_price

print(f"\nTotal ticket price for the family: ${total_price}")

# Prime
participants = []

while True:
    name = input("Enter the name of the participant (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    age_input = input("Enter the age of a participant : ")
    age = int(age_input)

    if 16 <= age <= 21:
        participants.append(name)
    else:
        print(f"Sorry, age {age} is not allowed for this movie.")

print("\nFinal list of participants allowed in the movie:")
print(participants)



