# 🎯 Scenario: Medical Image Classification
# You’re training a convolutional neural network (CNN) to detect pneumonia from chest X-rays.
# - Training accuracy: 95%
# - Validation accuracy: 74%
# At first glance, the model seems powerful — it almost perfectly classifies the training set. But the sharp drop in validation accuracy signals overfitting: the network has memorized the training images (specific pixel patterns, noise, or even hospital-specific artifacts) instead of learning generalizable features of pneumonia.

# ⚙️ Levers to Address Overfitting
# - Data Augmentation: Rotate, flip, and adjust brightness of X-rays to simulate variability.
# - Regularization: Apply dropout in dense layers or L2 weight decay.
# - Transfer Learning: Use a pretrained backbone (e.g., ResNet) to leverage generalized features.
# - Cross-validation: Ensure robustness across different patient subsets.
# - Early Stopping: Halt training when validation loss stops improving.

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# Create Synthetic Dataset
# -----------------------------
IMG_SIZE = 64
NUM_SAMPLES = 2000

X = []
y = []

for i in range(NUM_SAMPLES):

    # base random noise image
    img = np.random.normal(0.5, 0.2, (IMG_SIZE, IMG_SIZE, 1))

    if i < NUM_SAMPLES//2:
        # NORMAL class
        label = 0
    else:
        # PNEUMONIA class → add bright patch
        label = 1
        x = np.random.randint(10,50)
        y_pos = np.random.randint(10,50)
        img[x:x+8, y_pos:y_pos+8] += 1

    X.append(img)
    y.append(label)

X = np.array(X)
y = np.array(y)

# normalize
X = np.clip(X,0,1)

# -----------------------------
# Train Validation Split
# -----------------------------
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Data Augmentation
# -----------------------------
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    horizontal_flip=True
)

datagen.fit(X_train)

# -----------------------------
# CNN Model
# -----------------------------
model = Sequential([

    Conv2D(32,(3,3),activation='relu',input_shape=(64,64,1)),
    MaxPooling2D(2,2),

    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128,(3,3),activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),

    Dense(128,activation='relu'),
    Dropout(0.5),

    Dense(1,activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# -----------------------------
# Early Stopping
# -----------------------------
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

# -----------------------------
# Train Model
# -----------------------------
history = model.fit(
    datagen.flow(X_train,y_train,batch_size=32),
    validation_data=(X_val,y_val),
    epochs=5,
    callbacks=[early_stop]
)

# -----------------------------
# Plot Accuracy
# -----------------------------
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(["Train","Validation"])
plt.title("Accuracy")
plt.show()

# -----------------------------
# Predictions
# -----------------------------
pred = model.predict(X_val)
pred = (pred>0.5).astype(int)

print(confusion_matrix(y_val,pred))
print(classification_report(y_val,pred))
