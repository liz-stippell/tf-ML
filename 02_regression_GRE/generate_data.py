import random
import numpy as np

# Range for Verbal: 155+
# Range for Quantitative: 159+

# Possible range: 147 - 170

# Generate dataset of 100 points:
dataset = 1000

# Generate random data:
verbal_data = []
for i in range(dataset):
    verbal_data.append(random.randrange(130, 170, 1))

quantitative_data = []
for i in range(dataset):
    quantitative_data.append(random.randrange(130, 170, 1))

# Write data to files:
#file = open("verbal_data.txt", "w")
#for item in verbal_data:
#    file.write(str(item)+"\n")
#file.close()

#file = open("quantitative_data.txt", "w")
#for item in quantitative_data:
#    file.write(str(item)+"\n")
#file.close()


# Generate the data and write to a single file:
file = open("combined_data.txt", "w")
for i in range(0, dataset):
    file.write(str(verbal_data[i]) + "  " + str( quantitative_data[i]) + "\n")
file.close()

file = open("admit_data.txt", "w")
for i in range (0, dataset):
    if verbal_data[i] < 155:
        if quantitative_data[i] < 159:
            file.write("0 \n")
        if quantitative_data[i] >= 159:
            file.write("1 \n")

    if verbal_data[i] >= 155:
        if quantitative_data[i] < 159:
            file.write("1 \n")
        if quantitative_data[i] >= 159:
            file.write("2 \n")
file.close()
