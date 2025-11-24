# Exercice 1, 2 & 3
birthdays = {
    "bouchra": "2002/09/26",
    "nour": "2009/05/08",
    "nazha": "1990/05/19",
    "yahya": "2013/03/30",
    "yasser": "2003/09/29"
}

print("Welcome to the birthday dictionary!")
print("You can look up the birthdays of the people in the list!")

for name in birthdays.keys():
    print(f"- {name}")

print("Let's add a new birthday!")

new_name = input("Enter a new person's name: ").strip().lower()
new_birthday = input("Enter {new_name}'s birthday (YYYY/MM/DD): ").strip().lower()

birthdays[new_name] = new_birthday

print("Birthday added successfully!")
print("Here is an updated list: ")
for name in birthdays.keys():
    print(f"- {name}")

user_input = input("Enter a person's name to look up their birthday: ").strip().lower()

if user_input in birthdays:
    print(f"{name}'s birthday is: {birthdays[name]}")
else:
    print(f"Sorry, we don't have the birthday information for {user_input}.")

# Exercice 4
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for item, price in items.items():
    print(f"The price of {item} is ${price}")

items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0

for item, info in items.items():
    cost = info["price"] * info["stock"]
    print(f"{item.capitalize()}: ${cost}")
    total_cost += cost

print(f"Total cost to but everything is: ${total_cost}")

