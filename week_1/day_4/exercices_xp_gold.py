# Exercice 1
def get_age(year, month, day):
    current_year = 2025
    current_month = 11
    current_day = 24
    
    age = current_year - year

    if (month, day) > (current_month, current_day):
        age -= 1

    return age

def can_retire(gender, date_of_birth):
    year, month, day = date_of_birth.split("/")
    year = int(year)
    month = int(month)
    day = int(day)

    age = get_age(year, month, day)

    if gender == "m":
        return age >= 67
    elif gender == "f":
        return age >= 62
    else:
        return False

gender = input("Enter your gender (m/f): ").lower()
dob = input("Enter your date of birth (yyyy/mm/dd) : ")

if can_retire(gender, dob):
    print("You can retire!")
else:
    print("You cannot retire yet.")

# Exercice 2
def special_sum(x):
    x = str(x)
    return int(x) + int(x*2) + int(x*3) + int(x*4)

y = special_sum(3)
print(y)
# Exercice 3
import random

def throw_dice():
    return random.randint(1,6)

def throw_until_doubles():
    count = 0

    while True:
        count += 1
        d1 = throw_dice()
        d2 = throw_dice()

        print(f"Throw {count}: ({d1}, {d2})")

        if d1 == d2:
            break

    return count

def main():
    results = []

    for n in range(100):
        throws = throw_until_doubles()
        results.append(throws)

    total_throws = sum(results)
    average_throws = round(total_throws / 100, 2)

    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws}")


main()



# Exercice 4
# Exercice 5
# Exercice 6
# Exercice 7