import matplotlib.pyplot as plt
import numpy as np

# Create scatter plot with all the results
x = np.loadtxt("combined_data.txt")[:,0]
y = np.loadtxt("combined_data.txt")[:,1]

plt.plot(x, y, "o")
plt.ylabel("Verbal")
plt.xlabel("Quantitative")

plt.savefig("scores_plot.png")


# Create scatter plot of Quantitative Scores vs. Admissions
y = np.loadtxt("combined_data.txt")[:,0]
x = np.loadtxt("admit_data.txt")[:]

print(y)
print(x)

plt.plot(x, y, "o")
plt.ylabel("Quantitative")
plt.xlabel("Admission")

plt.savefig("quant.png")

# Create scatter plot of Verbal Scores vs. Admissions
y = np.loadtxt("combined_data.txt")[:,1]
x = np.loadtxt("admit_data.txt")[:]

plt.plot(x, y, "o")
plt.ylabel("Verbal")
plt.xlabel("Admission")

plt.savefig("verbal.png")
