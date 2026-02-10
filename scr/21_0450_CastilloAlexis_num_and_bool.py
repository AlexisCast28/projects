# ==================================================
# Problem 1: Temperature converter and range flag
# ==================================================
# Description:
# This program converts a temperature from Celsius
# to Fahrenheit and Kelvin, and checks if it is high.
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - Fahrenheit
# - Kelvin
# - High temperature (True or False)
#
# Validations:
# - Must be a valid float
# - Must not be below absolute zero
#
# Test cases:
# 1) Normal: 25
# 2) Edge: 30
# 3) Error: -300

temp_text = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_text)

    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"High temperature: {is_high_temperature}")

except:
    print("Error: invalid input")


# ==================================================
# Problem 2: Work hours and overtime payment
# ==================================================
# Description:
# This program calculates weekly pay including overtime.
#
# Inputs:
# - hours_worked (int)
# - hourly_rate (float)
#
# Outputs:
# - Regular pay
# - Overtime pay
# - Total pay
# - Has overtime
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Test cases:
# 1) Normal: 45, 100
# 2) Edge: 40, 80
# 3) Error: -5, 50

hours_text = input("Enter hours worked: ")
rate_text = input("Enter hourly rate: ")

try:
    hours_worked = int(hours_text)
    hourly_rate = float(rate_text)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = hours_worked > 40

        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {has_overtime}")

except:
    print("Error: invalid input")


# ==================================================
# Problem 3: Discount eligibility with booleans
# ==================================================
# Description:
# Determines if a customer gets a discount.
#
# Inputs:
# - purchase_total (float)
# - is_student_text ("YES" or "NO")
# - is_senior_text ("YES" or "NO")
#
# Outputs:
# - Discount eligible
# - Final total
#
# Validations:
# - purchase_total >= 0
# - YES or NO values only
#
# Test cases:
# 1) Normal: 1200, NO, NO
# 2) Edge: 500, YES, NO
# 3) Error: 300, MAYBE, NO

total_text = input("Enter purchase total: ")
student_text = input("Is student (YES/NO): ").strip().upper()
senior_text = input("Is senior (YES/NO): ").strip().upper()

try:
    purchase_total = float(total_text)

    if purchase_total < 0:
        print("Error: invalid input")
    elif student_text not in ["YES", "NO"] or senior_text not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        is_student = student_text == "YES"
        is_senior = senior_text == "YES"

        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total}")

except:
    print("Error: invalid input")


# ==================================================
# Problem 4: Basic statistics of three integers
# ==================================================
# Description:
# Calculates statistics from three integers.
#
# Inputs:
# - n1, n2, n3 (int)
#
# Outputs:
# - Sum
# - Average
# - Max
# - Min
# - All even
#
# Validations:
# - Must be integers
#
# Test cases:
# 1) Normal: 2, 4, 6
# 2) Edge: 1, 2, 3
# 3) Error: a, 3, 5

n1_text = input("Enter first integer: ")
n2_text = input("Enter second integer: ")
n3_text = input("Enter third integer: ")

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")

except:
    print("Error: invalid input")


# ==================================================
# Problem 5: Loan eligibility
# ==================================================
# Description:
# Checks if a person is eligible for a loan.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - Debt ratio
# - Eligible
#
# Validations:
# - monthly_income > 0
# - monthly_debt >= 0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: 12000, 3000, 700
# 2) Edge: 8000, 3200, 650
# 3) Error: 0, 1000, 600

income_text = input("Enter monthly income: ")
debt_text = input("Enter monthly debt: ")
score_text = input("Enter credit score: ")

try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and
                    debt_ratio <= 0.4 and
                    credit_score >= 650)

        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible: {eligible}")

except:
    print("Error: invalid input")


# ==================================================
# Problem 6: Body Mass Index (BMI)
# ==================================================
# Description:
# Calculates BMI and determines category.
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - BMI
# - Underweight
# - Normal
# - Overweight
#
# Validations:
# - weight_kg > 0
# - height_m > 0
#
# Test cases:
# 1) Normal: 70, 1.75
# 2) Edge: 50, 1.60
# 3) Error: -70, 1.80

weight_text = input("Enter weight in kg: ")
height_text = input("Enter height in meters: ")

try:
    weight_kg = float(weight_text)
    height_m = float(height_text)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {bmi}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")

except:
    print("Error: invalid input")
