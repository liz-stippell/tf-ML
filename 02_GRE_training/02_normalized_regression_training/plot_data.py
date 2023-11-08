import matplotlib.pyplot as plt
import numpy as np

# Create scatter plot with all the results
x = np.loadtxt("combined_data.txt")[:,0]
y = np.loadtxt("combined_data.txt")[:,1]

plt.plot(x, y, "o")
plt.ylabel("Verbal")
plt.xlabel("Quantitative")

plt.savefig("scores_plot.png")

plt.clf()

# Create scatter plot of Quantitative Scores vs. Admissions
y_quant = np.loadtxt("combined_data.txt")[:,0]
x_quant = np.loadtxt("admit_data.txt")[:]

plt.plot(x_quant, y_quant, "o")
plt.ylabel("Quantitative")
plt.xlabel("Admission")

plt.savefig("quant.png")

plt.clf()

# Create scatter plot of Verbal Scores vs. Admissions
y_verb = np.loadtxt("combined_data.txt")[:,1]
x_verb = np.loadtxt("admit_data.txt")[:]

plt.plot(x_verb, y_verb, "o")
plt.ylabel("Verbal")
plt.xlabel("Admission")

plt.savefig("verbal.png")
