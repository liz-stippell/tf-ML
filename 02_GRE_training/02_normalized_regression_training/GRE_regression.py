import tensorflow as tf
import numpy as np
from tensorflow import keras

print(tf.__version__)

# Build a simple Sequential model
model = tf.keras.Sequential([
  keras.layers.Dense(units=64, input_shape=[2], activation="relu"),
  keras.layers.Dense(units=32, activation="relu"),
  keras.layers.Dense(units=1) #, activation="softmax")
])

# Compile the model
#model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=["accuracy"])

model.compile(optimizer='sgd', loss='mean_squared_error')

# Declare model inputs and outputs for training
x_train = np.loadtxt("normalized_data.txt") #[:,0]
y_train = np.loadtxt("normalized_admit_data.txt")

print(np.shape(x_train))

#x_train = np.array([140, 150, 155,  160, 170])
#y_train = np.array([0.00, 0.10, 0.50, 0.90, 1.00])

#x_train = np.array([1.0, 2.0, 3.0, 4.0])
#y_train = np.array([5.0, 8.0, 11.0, 14.0])

# Train the model
model.fit(x_train, y_train, epochs=100)

min_val = 130
range_val = 40

val_1 = (170 - min_val)/range_val
val_2 = (170 - min_val)/range_val
prediction = np.array([[val_1, val_2]]) #.reshape(1, 2)

print(np.shape(prediction))

# Make a prediction
print(f"Prediction for {prediction}: " + str(model.predict(prediction)))
#predicted_class = np.argmax(model.predict(prediction))
#print(predicted_class)

# Evaluate the model
loss = model.evaluate(x_train, y_train)
tf.print(f'Loss: {loss}')
