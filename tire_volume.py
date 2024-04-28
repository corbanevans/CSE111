import math

def calculate_v(w, a, d):
    numerator = (math.pi * w ** 2 * a * (w * a + 2540 * d))
    denominator = 10_000_000_000
    v = numerator / denominator
    v = round(v, 2)

    print("The approximate volume of the tire is:", v, "liters")

d = float(input("Enter the diameter of the tire (in inches): "))
w = float(input("Enter the width of the tire (in millimeters): "))
a = float(input("Enter the aspect ratio of the tire: "))

calculate_v(w, a, d)