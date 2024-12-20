import math

# 1. String Manipulation
s1 = "Maha Bharat"
print("a.", s1.swapcase())
print("b.", s1[5:])
print("c.", s1[5:] * 3)
print("d.", "Mera " + s1[5:])
print("e.", "Mera " + s1 + " Mahan")

# 2. String Analysis
s = "Ba Ba Black Sheep"
print("a.", len(s))
print("b.", s.find('e'))
print("c.", s.count('a'))
print("d.", s.replace("Ba", "Ta", 1))

# 3. Palindrome Check
str_inp = input("enter string: ")
print("palindrome:", str_inp == str_inp[::-1])

# 4. Student Details
name = input("enter name: ")
roll_no = input("enter roll number: ")
marks = float(input("enter marks: "))
if marks >= 90:
    grade, remark = 10, "OUTSTANDING"
elif marks >= 80:
    grade, remark = 9, "VERY GOOD"
elif marks >= 70:
    grade, remark = 8, "GOOD"
elif marks >= 60:
    grade, remark = 7, "AVERAGE"
elif marks >= 50:
    grade, remark = 6, "PASS"
else:
    grade, remark = 0, "FAIL"
print(f"name: {name}, roll no: {roll_no}, marks: {marks}, grade: {grade}, remark: {remark}")

# 5. Roots of Quadratic Equation
a = int(input("enter coefficient a: "))
b = int(input("enter coefficient b: "))
c = int(input("enter coefficient c: "))
disc = b**2 - 4*a*c
if disc > 0:
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)
    print("roots are real and distinct:", root1, root2)
elif disc == 0:
    root = -b / (2 * a)
    print("roots are real and equal:", root)
else:
    real = -b / (2 * a)
    imag = math.sqrt(-disc) / (2 * a)
    print("roots are complex:", f"{real} + {imag}i", f"{real} - {imag}i")
