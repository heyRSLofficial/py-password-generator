# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
if nr_letters in range(1, 26) and nr_symbols in range(1, 26) and nr_numbers in range(1, 26):
    for l in range(nr_letters):
        password_list.append(random.choice(letters))
    for s in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for n in range(nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    print(''.join(password_list))
else:
    print("Seems like you either don't need a password or you are just playing around. \nPlease use it when you need an actual password & also with the inputs for each value only in this range(1,25).\nThank you!")
