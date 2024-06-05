import math
from datetime import datetime

def calculate_v(w, a, d):
    numerator = (math.pi * w ** 2 * a * (w * a + 2540 * d))
    denominator = 10_000_000_000
    v = numerator / denominator
    v = round(v, 2)
    print("The approximate volume of the tire is:", v, "liters")
    return v

d = float(input("Enter the diameter of the tire (in inches): "))
w = float(input("Enter the width of the tire (in millimeters): "))
a = float(input("Enter the aspect ratio of the tire: "))

v = calculate_v(w, a, d)

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Prepare the line to write to the file
line_to_write = f"{current_date}, {w}, {a}, {d}, {v}"
    
# Ask the user if they want to buy tires
buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()

if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ")
    line_to_write += f", {phone_number}"

# Open the file for appending and write the values
with open("volumes.txt", "a") as file:
    file.write(line_to_write + "\n")