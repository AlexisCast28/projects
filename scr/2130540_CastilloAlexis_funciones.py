# Problem 1: Rectangle area and perimeter
# Description:
# This program defines two functions to calculate
# the area and perimeter of a rectangle.

# Inputs:
# - width (float)
# - height (float)

# Outputs:
# - Area
# - Perimeter

# Validations:
# - width > 0
# - height > 0

# Test cases:
# 1) Normal: width=5, height=3
# 2) Edge case: width=0.1, height=0.1
# 3) Error: width=-2

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width_text = input("Enter width: ")
height_text = input("Enter height: ")

try:
    width = float(width_text)
    height = float(height_text)

    if width <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)

        print("Area:", area)
        print("Perimeter:", perimeter)

except:
    print("Error: invalid input")
