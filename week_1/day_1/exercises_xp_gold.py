# Exercice 1
print("Hello World\n" * 4 + "I love python\n" *4)

# Exercice 2
month = int(input("Enter a month number (1 to 12): "))
if 3 <= month <= 5:
    print(f"The seanson of month {month} is Spring")
elif 6 <= month <= 8:
    print(f"The seanson of month {month} is Summer")
elif 9 <= month <= 11:
    print(f"The seanson of month {month} is Autumn")
elif month == 12 or month == 1 or month == 2:
    print(f"The seanson of month {month} is Winter")
else:
    print("Invalid month!")



