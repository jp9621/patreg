import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load your data here (replace 'pattern_data_padded_shuffled.csv' with the actual file path)
data = pd.read_csv('st/st_data.csv', header=None)

# Separate features (X) and target variable (y)
X = data.iloc[:, 1:].values  # Features (excluding the first column)
y = data.iloc[:, 0].values    # Target variable (first column)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Reshape X_train and X_test to fit the LSTM input shape (samples, time steps, features)
# Assuming each sample is a time series with multiple features
n_features = X_train.shape[1]  # Number of features
X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])

# Build the LSTM model
model = Sequential([
    LSTM(64, input_shape=(1, n_features)),  # LSTM layer with 64 units
    Dense(1, activation='sigmoid')          # Output layer with sigmoid activation for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}')
print(f'Test Accuracy: {accuracy}')

# Save the trained model
model.save('stress-test/st/stressed_st_lstm.h5')
