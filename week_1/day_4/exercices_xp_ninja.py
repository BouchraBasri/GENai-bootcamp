# Exercice 1
def get_full_name(first_name, last_name, middle_name = ""):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    middle_name = middle_name.capitalize()

    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

print(get_full_name("Bouchra", "Azrour"))
# Exercice 2
MORSE_CODE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",
    "D": "-..",   "E": ".",     "F": "..-.",
    "G": "--.",   "H": "....",  "I": "..",
    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",
    "S": "...",   "T": "-",     "U": "..-",
    "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----.",

    " ": "/"   # space between words
}

REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}

def english_to_morse(text):
    text = text.upper()
    morse = []

    for char in text:
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
        else:
            morse.append("?")

    return " ".join(morse)

def morse_to_english(text):
    words = text.split(" ")
    english = []

    for symbol in words:
        if symbol in REVERSE_MORSE_CODE:
            english.append(REVERSE_MORSE_CODE[symbol])
        else:
            english.append("?")

    return "".join(english)

text = "Bouchra"
morse = english_to_morse(text)
decoded = morse_to_english(morse)

print("English: ", text)
print("Morse: ", morse)
print("Decoded: ", decoded)

# Exercice 3
def box_printer(*words):
    longest = max(len(word) for word in words)

    print("*" * (longest + 4))

    for word in words:
        padding = longest - len(word)
        print(f"* {word}{' ' * padding} *")

    print("*" * (longest + 4))

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Exercice 4
# It's an Insertion Sorting