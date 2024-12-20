import numpy as np

covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],
    [1600, 2100, 1900, 1300, 950],
    [1700, 2200, 2000, 1400, 1000],
    [1650, 2150, 1950, 1350, 980],
    [1750, 2250, 2050, 1450, 1020],
    [1800, 2300, 2100, 1500, 1050],
    [1900, 2400, 2200, 1600, 1100],
])

# 1. Basic statistics
total_cases = covid_data.sum(axis=0)
highest_cases = total_cases.argmax()
print("total cases:", total_cases)
print("country with highest cases:", highest_cases + 1)

# 2. Daily analysis
daily_avg = covid_data.mean(axis=1)
highest_day = daily_avg.argmax()
print("daily average:", daily_avg)
print("day with highest cases:", highest_day + 1)

# 3. Trends
percent_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
highest_increase = percent_change.argmax()
print("percentage changes:", percent_change)
print("highest increase:", highest_increase + 1)

# 4. Data normalization
norm_data = (covid_data - covid_data.min()) / (covid_data.max() - covid_data.min())
print("normalized data:", norm_data)

# 5. Visualization
import matplotlib.pyplot as plt

for i in range(covid_data.shape[1]):
    plt.plot(covid_data[:, i], label=f"Country {i+1}")
plt.legend()
plt.title("Daily Cases by Country")
plt.show()
