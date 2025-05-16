import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to Password generator.")
letter_user = int(input("How many letters do want to include:\n"))
numbers_user = int(input("How many numbers do want to include:\n"))
symbols_user = int(input("How many symbols do want to include:\n"))
password_list = []
for i in range(1, letter_user + 1):
    char = random.choice(letters)
    password_list += char
for i in range(1, numbers_user + 1):
    char = random.choice(numbers)
    password_list += char
for i in range(1, symbols_user + 1):
    char = random.choice(symbols)
    password_list += char
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for x in password_list:
    password = password + x
print(password)