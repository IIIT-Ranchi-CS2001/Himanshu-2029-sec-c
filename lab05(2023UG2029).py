# 1. Euclidean Distance
point1 = tuple(map(float, input("enter coordinates of point 1 (x y z): ").split()))
point2 = tuple(map(float, input("enter coordinates of point 2 (x y z): ").split()))
distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2) ** 0.5
print("distance:", distance)

# 5. Equation of a Straight Line
x1, y1 = map(float, input("enter coordinates of point 1 (x y): ").split())
x2, y2 = map(float, input("enter coordinates of point 2 (x y): ").split())
slope = (y2 - y1) / (x2 - x1)
print(f"line equation: y - {y1} = {slope}(x - {x1})")

# 6. Count Characters in a String
string = input("enter string: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("character counts:", char_count)

# 7. Customer Details as Tuples (with and without zip)
cust_names = input("enter customer names separated by space: ").split()
cust_ids = input("enter customer IDs separated by space: ").split()
cust_points = list(map(int, input("enter shopping points separated by space: ").split()))

# Using zip()
cust_details_zip = list(zip(cust_names, cust_ids, cust_points))
print("customer details using zip:", cust_details_zip)

# Without using zip()
cust_details_no_zip = [(cust_names[i], cust_ids[i], cust_points[i]) for i in range(len(cust_names))]
print("customer details without zip:", cust_details_no_zip)

# 8. Sorting Tuples (with and without sorted)
# Using sorted()
sorted_details = sorted(cust_details_no_zip, key=lambda x: x[2], reverse=True)
print("sorted customer details using sorted:", sorted_details)

# Without using sorted()
for i in range(len(cust_details_no_zip)):
    for j in range(i + 1, len(cust_details_no_zip)):
        if cust_details_no_zip[i][2] < cust_details_no_zip[j][2]:
            cust_details_no_zip[i], cust_details_no_zip[j] = cust_details_no_zip[j], cust_details_no_zip[i]
print("sorted customer details without sorted:", cust_details_no_zip)
