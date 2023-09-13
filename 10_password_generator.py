import random
# Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', ';']
letter_count = int(input("Enter the letter count : "))
number_count = int(input("Enter the number count : "))
symbol_count = int(input("Enter the symbol count : "))
letter_list = []
number_list = []
symbol_list = []

for i in range(0, letter_count) :
    letter = letters[random.randint(0, len(letters) - 1)]
    letter_list.append(letter)

for i in range(0, number_count) :
    number = numbers[random.randint(0, len(numbers) - 1)]
    number_list.append(number)

for i in range(0, symbol_count) :
    symbol = symbols[random.randint(0, len(symbols) - 1)]
    symbol_list.append(symbol)

character_list = letter_list + number_list + symbol_list
random.shuffle(character_list)

password = ""
for character in character_list :
    password += character

# password = "".join(character_list)

print(f"Generated Password : {password}")