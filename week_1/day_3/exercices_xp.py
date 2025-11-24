# Exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)    

# Exercice 2
family = {}
total_cost = 0

while True:
    name= input("Enter name (or type 'done' if you finished): ").strip().lower()

    if name == 'done':
        break

    age_input = input(f"Enter age of {name.capitalize()}: ")

    if not age_input.isdigit():
        print("Please enter a valid number for age.")
        continue

    age = int(age_input)

    family[name] = age

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name.capitalize()} pays: ${price}")
    total_cost += price

print(f"Total cost: ${total_cost}")

# Exercice 3
brand = {'name': 'zara', 
         'creation_date': 1975, 
         'creator_name': 'Amanco Ortega Gaona', 
         'type_of_clothes': ['man', 'women', 'children', 'home'], 
         'international_competitors': ['Gap', 'H&M', 'Benetton'], 
         'number_stores': 7000, 
         'major_color':{
            'France': 'blue',
            'Spain': 'red',
            'US': ['pink', 'green']
         }}

brand["number_stores"] = 2

print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")

brand["country_creation"] = 'Spain'

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand["inernational_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

print(brand.keys())

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 50000
}

brand.update(more_on_zara)
print(brand)

# Exercice 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

result = {char: index for index, char in enumerate(users)}
print(result)

result_2 = dict(enumerate(users))
print(result_2)

sorted_users = sorted(users)
result_3 = {char: index for index, char in enumerate(sorted_users)}
print(result_3)




