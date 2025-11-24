choice = input("Do you want to encrypt (e) or decrypt (d): ").lower()
text = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

result = ""

for letter in text:
    if letter.isalpha():
        if choice == "e":
            result += chr(ord(letter) + shift)
        else:
            result += chr(ord(letter) - shift)
    else:
        result += letter

print("Result: ", result)
