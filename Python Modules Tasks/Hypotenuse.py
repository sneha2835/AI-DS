import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
hypotenuse = math.sqrt(a**2 + b**2)
print(f"The hypotenuse of the triangle is: {hypotenuse:.2f}")
