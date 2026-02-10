# Problem 1: Sum of integers in a range
# Description:
# This program calculates the sum of numbers from 1 to n
# and also calculates the sum of even numbers in that range.

# Inputs:
# - n (int)

# Outputs:
# - Sum 1..n
# - Even sum 1..n

# Validations:
# - n must be an integer
# - n >= 1

# Test cases:
# 1) Normal: n = 5
# 2) Edge case: n = 1
# 3) Error: n = -3

n_text = input("Enter n: ")

try:
    n = int(n_text)

    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i

            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except:
    print("Error: invalid input")
