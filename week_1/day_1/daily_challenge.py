# Exercice 3
print( 3 <= 3 < 9 ) #True
print( 3 == 3 == 3) #True
print( bool(0) ) #False
print( bool(5 == "5")) #False
print( bool(4 == 4) == bool("4" == "4")) #True
print( bool(bool(None)) ) #False
x = (1 == True) #True
y = (1 == False) #False
a = True + 4 #5
b = False + 10 #10
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Exercice 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

# Exercice 5
longest_sentence = ""
while True:
    sentence = input("Enter the longest sentence you can without using letter 'A': ")
    
    if 'A' in sentence or 'a' in sentence:
        print("Your sentence contains 'A'.")
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congrats! New longest sentence set.")
    else: 
        print("Good try, But it's not longer than your previous longest one.")