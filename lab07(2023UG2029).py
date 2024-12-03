import matplotlib.pyplot as plt

# Q1: Party-wise seat share
mp_results = {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1}
rj_results = {"INC": 69, "BJP": 115, "BSP": 2, "Others": 13}

plt.pie(mp_results.values(), labels=mp_results.keys(), autopct='%1.1f%%', startangle=90)
plt.title("Madhya Pradesh Results")
plt.show()

plt.pie(rj_results.values(), labels=rj_results.keys(), autopct='%1.1f%%', startangle=90)
plt.title("Rajasthan Results")
plt.show()

# Bar chart
states = ['MP', 'RJ']
for party in mp_results:
    plt.bar(states, [mp_results[party], rj_results.get(party, 0)], label=party)
plt.legend()
plt.show()

# Q2: Random numbers scatter plot
import random, math

k = int(input("enter k: "))
n = int(input("enter limit n: "))
random_nums = [random.randint(1, n) for _ in range(k)]
primes = [x for x in random_nums if all(x % d != 0 for d in range(2, int(math.sqrt(x)) + 1))]
composites = [x for x in random_nums if x not in primes]

plt.scatter(primes, [x**2 for x in primes], label="Prime vs Squares")
plt.scatter(composites, [math.sqrt(x) for x in composites], label="Composite vs Square Roots")
plt.legend()
plt.show()
