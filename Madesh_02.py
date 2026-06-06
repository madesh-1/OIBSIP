def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")


print("===== BMI Calculator =====")

weight = get_valid_input("Enter your weight (kg): ", 1, 500)
height = get_valid_input("Enter your height (meters): ", 0.5, 3.0)

bmi = calculate_bmi(weight, height)
category = classify_bmi(bmi)

print(f"\nYour BMI: {bmi}")
print(f"Category: {category}")
