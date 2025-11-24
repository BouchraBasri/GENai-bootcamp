# Challenge 1
word = input("Enter a word: ")

dictionary = {}

for index, char in enumerate(word):
    if char in dictionary:
        dictionary[char].append(index)
    else:
        dictionary[char] = [index]

print(dictionary)

# Challenge 2
items_purchase = {
    "phone": "$999",
    "spreads": "$300",
    "laptop": "$5000",
    "pc": "$1200"
}

wallet = "$1"

money = int(wallet.replace("$","").replace(",",""))

cleaned_items = {}

for item, price_str in items_purchase.items():
    price = int(price_str.replace("$","").replace(",",""))
    cleaned_items[item] = price

basket = []
for item, price in cleaned_items.items():
    if money >= price:
        basket.append(item)
        money -= price

if not basket:
    print("Nothing")
else:
    print("You bought: ", sorted(basket))
    print("Money left:", money)

