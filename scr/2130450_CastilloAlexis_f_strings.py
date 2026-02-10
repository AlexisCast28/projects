# ==================================================
# Problem 1: Full name formatter (name + initials)
# ==================================================
# Description:
# This program receives a full name as a string.
# It cleans extra spaces, formats it to Title Case
# and prints the initials of each word.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - Formatted name
# - Initials
#
# Validation:
# - The name must not be empty after strip()
# - The name must contain at least two words
#
# Test cases:
# 1) Normal: "juan carlos tovar"
# 2) Edge: "   ana lopez   "
# 3) Error: "   "

full_name = input("Enter a full name: ")

full_name = full_name.strip()

if full_name == "":
    print("Error: invalid input")
else:
    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("Error: invalid input")
    else:
        formatted_name = full_name.title()
        initials = ""

        for word in name_parts:
            initials += word[0].upper() + "."

        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")


# ==================================================
# Problem 2: Simple email validator
# ==================================================
# Description:
# This program checks if an email has a basic format.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - Valid email: True / False
# - Domain if valid
#
# Validation:
# - Must not be empty
# - Must contain exactly one '@'
# - Must not contain spaces
#
# Test cases:
# 1) Normal: "user@test.com"
# 2) Edge: "a@b.c"
# 3) Error: "user test.com"

email_text = input("Enter an email: ")
email_text = email_text.strip()

is_valid = True

if email_text == "":
    is_valid = False
if email_text.count("@") != 1:
    is_valid = False
if " " in email_text:
    is_valid = False
if:
    domain_part = email_text.split("@")[1]:
    if "." not in email_text.split("@")[1]:
        is_valid = False


print(f"Valid email: {is_valid}")

if is_valid:
    at_position = email_text.find("@")
    domain = email_text[at_position + 1:]
    print(f"Domain: {domain}")


# ==================================================
# Problem 3: Palindrome checker
# ==================================================
# Description:
# Checks if a phrase is a palindrome ignoring
# spaces and letter case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - Is palindrome: true / false
#
# Validation:
# - Not empty after strip()
# - At least 3 characters after cleaning
#
# Test cases:
# 1) Normal: "Anita lava la tina"
# 2) Edge: "oso"
# 3) Error: "  "

phrase = input("Enter a phrase: ")
phrase = phrase.strip()

if phrase == "":
    print("Error: invalid input")
else:
    cleaned_phrase = phrase.lower().replace(" ", "")

    if len(cleaned_phrase) < 3:
        print("Error: invalid input")
    else:
        reversed_phrase = cleaned_phrase[::-1]

        if cleaned_phrase == reversed_phrase:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")


# ==================================================
# Problem 4: Sentence word statistics
# ==================================================
# Description:
# Shows statistics about a sentence.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Word count
# - First and last word
# - Shortest and longest word
#
# Validation:
# - Sentence must not be empty
#
# Test cases:
# 1) Normal: "Python is very powerful"
# 2) Edge: "Hello"
# 3) Error: "   "

sentence = input("Enter a sentences: ")
sentence = sentence.strip()

if sentence == "":
    print("Error: invalid input")
else:
    words = sentence.split()

    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ==================================================
# Problem 5: Password strength classifier
# ==================================================
# Description:
# Classifies a password as weak, medium or strong.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - Password strength
#
# Validation:
# - Must not be empty
#
# Test cases:
# 1) Normal: "Abc123!"
# 2) Edge: "password"
# 3) Error: ""

password_input = input("Enter a password: ")
password_input = password_input.strip()

if password_input == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")


# ==================================================
# Problem 6: Product label formatter
# ==================================================
# Description:
# Creates a fixed-width label of exactly 30 characters.
#
# Inputs:
# - product_name (string)
# - price_value (number or string)
#
# Outputs:
# - Label
#
# Validation:
# - Product name not empty
# - Price must be positive
#
# Test cases:
# 1) Normal: "Keyboard", 25.5
# 2) Edge: "Pen", 1
# 3) Error: "", -3

product_name = input("Enter product name: ")
price_value = 25.5

product_name = product_name.strip()

if product_name == "":
    print("Error: invalid input")
else:
    if price_value <= 0:
        print("Error: invalid input")
    else:
        label = f"Product: {product_name} | Price: ${price_value}"

        if len(label) > 30:
            label = label[:30]
        else:
            label = label + " " * (30 - len(label))

        print(f'Label: "{label}"')
