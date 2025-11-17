from datetime import datetime

birthdate_str = input("Enter your birthday (DD/MM/YYYY)")

birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
today = datetime.today()
age = today.year - birthdate.year

if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

candles_count = age % 10
candles = "i" * candles_count
year = birthdate.year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def print_cake():
    print(f"        ____{candles}____")
    print("        |:H:a:p:p:y|")
    print("      __|__________|__")
    print("     |^^^^^^^^^^^^^^^^|")
    print("     |:B:i:r:t:h:d:a:y|")
    print("     |                |")
    print("     ~~~~~~~~~~~~~~~~~~")

if is_leap:
    print("\n🎉 You were born in a leap year! Double celebration! 🎉\n")
    print_cake()
    print_cake()
else:
    print_cake()