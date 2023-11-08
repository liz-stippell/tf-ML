import numpy as np

verbal_data = np.loadtxt("combined_data.txt")[:,0]
quant_data = np.loadtxt("combined_data.txt")[:,1]
admit_data = np.loadtxt("admit_data.txt")

def normalize_data(filename, min_val, range_val, data1, data2 = None):
    file = open(f"{filename}.txt", "w")
    for i in range(0, len(data1)):
        # To normalize data, take the data point, subtract the lowest possible value (130), then divide this by the range for the data (170 - 130 = 40)
        normalized_data1 = (data1[i] - min_val)/range_val
        if data2 is not None:
            normalized_data2 = (data2[i]-130)/40
            file.write(f"{normalized_data1}  {normalized_data2} \n")
        else:
            file.write(f"{normalized_data1} \n")
    file.close()

normalize_data("normalized_data", 130, 40, verbal_data, quant_data)
normalize_data("normalized_admit_data", 0, 2, admit_data)
