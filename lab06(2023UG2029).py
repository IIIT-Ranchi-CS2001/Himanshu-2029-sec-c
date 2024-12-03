# 1. Custom zip function
def my_zip(*args, strct=False):
    min_len = min(len(arg) for arg in args)
    if strct and not all(len(arg) == min_len for arg in args):
        return []
    return [(args[i][j] for i in range(len(args))) for j in range(min_len)]

# 2. Custom sorting function
def my_sort(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

# 3. Custom max function
def my_max(*args):
    maximum = args[0]
    for value in args[1:]:
        if value > maximum:
            maximum = value
    return maximum

# 4. Using lambda, map, filter
string = input("enter string: ")
letters = list(map(str.upper, filter(str.isalpha, string)))
digits = list(map(lambda x: int(x)**2, filter(str.isdigit, string)))
alphanum = list(filter(str.isalnum, string))
print("letters:", letters)
print("digits:", digits)
print("alphanumeric:", alphanum)
