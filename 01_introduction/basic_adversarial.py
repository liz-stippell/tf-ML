import numpy as np
import tensorflow as tf

# Define your data
X_correct = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
X_incorrect = np.array([8.0, 11.0, 12.0, 13.0, 14.0, 15.0])

y_correct = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0])
y_incorrect = np.array([18.0, 19.0, 20.0, 21.0, 22.0, 23.0])

# Combine the data
X = np.concatenate((X_correct, X_incorrect))
y = np.concatenate((y_correct, y_incorrect))

# Create and compile the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=10000, batch_size=32)

# Evaluate the model
loss = model.evaluate(X, y)
print(f'Loss: {loss}')

# Test the model

print(model.predict([10.0]))

# Assuming you have already trained your model

# Define the input value you want to predict
input_value = np.array([10.0])

# Make the prediction
predicted_value = model.predict(input_value)

print(f"The model predicts {predicted_value[0][0]} for X_correct = 10.0")

