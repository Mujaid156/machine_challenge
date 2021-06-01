import matplotlib.pyplot as plt

nums = [0.5, 0.7, 1.0, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

plt.hist(nums, bins, color='red', edgecolor='yellow', linewidth=5)
plt.xlabel("Numbers")
plt.ylabel("Bins")
plt.title("Histogram")
plt.show()
