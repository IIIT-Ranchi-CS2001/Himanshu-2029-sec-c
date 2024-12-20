# 1. Palindrome words count
sentence = input("enter sentence: ")
words = sentence.split()
palindromes = [word for word in words if word == word[::-1]]
print("number of palindromes:", len(palindromes))

# 2. Mean, median, and mode without libraries
nums = list(map(int, input("enter numbers separated by space: ").split()))
nums.sort()
mean = sum(nums) / len(nums)
median = nums[len(nums) // 2] if len(nums) % 2 != 0 else (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
mode = max(set(nums), key=nums.count)
print("mean:", mean)
print("median:", median)
print("mode:", mode)

# 3. Combine course codes and names
codes = input("enter course codes separated by space: ").split()
names = input("enter course names separated by space: ").split()
combined = [f"{code}:{name}" for code, name in zip(codes, names)]
print(combined)

# 4. Set operations
singers = {name for name in input("enter singers separated by space: ").split()}
dancers = {name for name in input("enter dancers separated by space: ").split()}
artists = singers | dancers
allrounders = singers & dancers
only_dancers = dancers - singers
only_singers = singers - dancers
print("artists:", artists)
print("allrounders:", allrounders)
print("only dancers:", only_dancers)
print("only singers:", only_singers)
