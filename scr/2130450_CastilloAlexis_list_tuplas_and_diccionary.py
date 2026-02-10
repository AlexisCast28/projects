# ==================================================
# Problem 1: Shopping list basics (list operations)
# ==================================================
# Description:
# This program works with a shopping list using a list.
# It allows adding items, counting items and searching.
#
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - Items list
# - Total items
# - Found item
#
# Validations:
# - Initial list not empty
# - new_item and search_item not empty
#
# Test cases:
# 1) Normal: "apple,banana,orange"
# 2) Edge: " apple , banana "
# 3) Error: ""

initial_items_text = input("Enter initial items (comma separated): ").strip()

if initial_items_text == "":
    print("Error: invalid input")
else:
    raw_items = initial_items_text.split(",")
    items_list = []

    for item in raw_items:
        cleaned_item = item.strip().lower()
        if cleaned_item != "":
            items_list.append(cleaned_item)

    new_item = input("Enter new item to add: ").strip().lower()
    search_item = input("Enter item to search: ").strip().lower()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        items_list.append(new_item)
        is_in_list = search_item in items_list

        print(f"Items list: {items_list}")
        print(f"Total items: {len(items_list)}")
        print(f"Found item: {is_in_list}")


# ==================================================
# Problem 2: Points and distances with tuples
# ==================================================
# Description:
# This program creates two points using tuples
# and calculates distance and midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - Point A
# - Point B
# - Distance
# - Midpoint
#
# Validations:
# - All values must be float
#
# Test cases:
# 1) Normal: 0,0,3,4
# 2) Edge: 1,1,1,1
# 3) Error: a,b,1,2

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")

except:
    print("Error: invalid input")


# ==================================================
# Problem 3: Product catalog with dictionary
# ==================================================
# Description:
# This program uses a dictionary as a product catalog.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - Unit price
# - Quantity
# - Total
#
# Validations:
# - product exists
# - quantity > 0
#
# Test cases:
# 1) Normal: apple, 3
# 2) Edge: banana, 1
# 3) Error: milk, 2

product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}

product_name = input("Enter product name: ").strip().lower()
quantity_text = input("Enter quantity: ")

try:
    quantity = int(quantity_text)

    if product_name == "" or quantity <= 0:
        print("Error: invalid input")
    elif product_name not in product_prices:
        print("Error: product not found")
    else:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print(f"Unit price: {unit_price}")
        print(f"Quantity: {quantity}")
        print(f"Total: {total_price}")

except:
    print("Error: invalid input")


# ==================================================
# Problem 4: Student grades with dict and list
# ==================================================
# Description:
# This program calculates the average grade of a student.
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - Grades
# - Average
# - Passed
#
# Validations:
# - Student exists
# - Grades list not empty
#
# Test cases:
# 1) Normal: Alice
# 2) Edge: Bob
# 3) Error: John

grades = {
    "alice": [90, 85, 88],
    "bob": [70, 72],
    "carol": [60, 65, 68]
}

student_name = input("Enter student name: ").strip().lower()

if student_name == "":
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
else:
    grades_list = grades[student_name]

    if len(grades_list) == 0:
        print("Error: invalid input")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0

        print(f"Grades: {grades_list}")
        print(f"Average: {average}")
        print(f"Passed: {is_passed}")


# ==================================================
# Problem 5: Word frequency counter
# ==================================================
# Description:
# This program counts word frequency in a sentence.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Words list
# - Frequencies
# - Most common word
#
# Validations:
# - Sentence not empty
#
# Test cases:
# 1) Normal: "Hello world hello"
# 2) Edge: "Hi"
# 3) Error: ""

sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    cleaned_sentence = sentence.lower()
    for char in ".,!?;:":
        cleaned_sentence = cleaned_sentence.replace(char, "")

    words_list = cleaned_sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = ""
        max_count = 0

        for word in freq_dict:
            if freq_dict[word] > max_count:
                max_count = freq_dict[word]
                most_common_word = word

        print(f"Words list: {words_list}")
        print(f"Frequencies: {freq_dict}")
        print(f"Most common word: {most_common_word}")


# ==================================================
# Problem 6: Simple address book (dictionary CRUD)
# ==================================================
# Description:
# This program manages a simple address book.
#
# Inputs:
# - action_text (ADD, SEARCH, DELETE)
# - name
# - phone (for ADD)
#
# Outputs:
# - Result message
#
# Validations:
# - Valid action
# - Name not empty
#
# Test cases:
# 1) Normal: ADD, Alice, 12345
# 2) Edge: SEARCH, Bob
# 3) Error: DELETE, John

contacts = {
    "alice": "123456789",
    "bob": "987654321"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid input")
else:
    name = input("Enter contact name: ").strip().lower()

    if name == "":
        print("Error: invalid input")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()
            if phone == "":
                print("Error: invalid input")
            else:
                contacts[name] = phone
                print(f"Contact saved: {name} {phone}")

        elif action_text == "SEARCH":
            if name in contacts:
                print(f"Phone: {contacts[name]}")
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print(f"Contact deleted: {name}")
            else:
                print("Error: contact not found")
