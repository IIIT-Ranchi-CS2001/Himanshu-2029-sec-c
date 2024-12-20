# 1. Arithmetic Operations
x = float(input("enter first number: "))
y = float(input("enter second number: "))
print("sum:", x + y)
print("difference:", x - y)
print("product:", x * y)
print("integer quotient:", x // y)
print("remainder:", x % y)
print("fractional quotient:", x / y)

# 2. Triangle Area, Perimeter, and Angles
s1 = float(input("enter side 1: "))
s2 = float(input("enter side 2: "))
s3 = float(input("enter side 3: "))
semi_p = (s1 + s2 + s3) / 2
area = (semi_p * (semi_p - s1) * (semi_p - s2) * (semi_p - s3)) ** 0.5
print("area:", area)
print("perimeter:", s1 + s2 + s3)

import math
angle1 = math.degrees(math.acos((s2**2 + s3**2 - s1**2) / (2 * s2 * s3)))
angle2 = math.degrees(math.acos((s1**2 + s3**2 - s2**2) / (2 * s1 * s3)))
angle3 = 180 - (angle1 + angle2)
print("angles:", angle1, angle2, angle3)

# 3. Impedance in Parallel
real1 = float(input("enter real part of z1: "))
imag1 = float(input("enter imaginary part of z1: "))
real2 = float(input("enter real part of z2: "))
imag2 = float(input("enter imaginary part of z2: "))
z1 = complex(real1, imag1)
z2 = complex(real2, imag2)
z_eq = 1 / (1 / z1 + 1 / z2)
print("z1:", z1)
print("z2:", z2)
print("equivalent impedance:", z_eq)
print("real part:", z_eq.real)
print("imaginary part:", z_eq.imag)
