import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        print("You must select at least one character type!")
        return None

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password

def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        print("Please enter yes or no.")

# Main program
print("===== Random Password Generator =====")

while True:
    try:
        length = int(input("Enter password length (4 to 50): "))
        if 4 <= length <= 50:
            break
        else:
            print("Please enter a length between 4 and 50.")
    except ValueError:
        print("Invalid input! Please enter a number.")

use_letters = get_yes_no("Include letters? (yes/no): ")
use_numbers = get_yes_no("Include numbers? (yes/no): ")
use_symbols = get_yes_no("Include symbols? (yes/no): ")

password = generate_password(length, use_letters, use_numbers, use_symbols)

if password:
    print(f"\nGenerated Password: {password}")
