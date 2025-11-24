# Exercice 1
def display_message():
    print("I'm learning about functions in Python")

display_message()

# Exercice 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# Exercice 3
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# Exercice 4
import random

def random_numbers(number):
    r_number = random.randint(1, 100)

    if r_number == number:
        print("Success")
    else:
        print(f"Fail! Your number: {number}, Random number: {r_number}")

random_numbers(23)

# Exercice 5
def make_shirt(size = "Large", text = "I love Python."):
    print(f"The size of the shirt is {size} and the text is {text}\n")

make_shirt("medium", "Hello world!")

make_shirt()
make_shirt("medium")
make_shirt("small","Custom message")

make_shirt(size = "small", text = "Hello!")

# Exercice 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    modified_list = []
    for magician in magicians:
        modified_list.append("The Great " + magician)    
    return modified_list

magician_names = make_great(magician_names)
show_magicians(magician_names)

# Exercice 7
import random

def get_random_temp(season):
    if season == "Winter":
        return round(random.uniform(-10, 10), 1)
    elif season == "Spring":
        return round(random.uniform(5, 20), 1)
    elif season == "Summer":
        return round(random.uniform(20, 40), 1)
    else:
        return round(random.uniform(5, 25), 1)

def main():
    month = int(input("Enter the month number (1-12): "))

    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    else:
        season = "Fall"

    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature <= 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 < temperature <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temperature <= 23:
        print("Nice weather.")
    elif 23 < temperature <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()