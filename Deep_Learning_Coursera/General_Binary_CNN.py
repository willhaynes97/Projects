#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import zipfile
import math
import tensorflow as tf
from tensorflow import keras

"""
Hyperparameters
"""
# Location of the training zip
train_zip_location = input('What is the location of the training zip?: ')
train_location = train_zip_location[:-4]

# Location of the validation zip
val_zip_location = input('What is the location of the validation zip?: ')
val_location = val_zip_location[:-4]

# First classification name
input('What is the name of the first classification?: ')

#Second classification name
input('What is the name of the second classification?: ')

# Define the number of convolutional layers
NUM_OF_CONV_LAYERS = int(input('Number of convolution layers (at least 1): '))

# Define the number of hidden deep layers
NUM_OF_HIDDEN_LAYERS = int(input('Number of hidden layers (at least 1): '))

# Input Image size
IMAGE_SIZE = int(input('Target size of images: '))

# Training batch size
TRAIN_BATCH_SIZE = 128

# Validation batch size
VAL_BATCH_SIZE = 32

"""
Loading File
"""
# load zip of Training data and unzip
local_zip = train_zip_location
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall(train_location)

# load zip of Validation data and unzip
local_zip = val_zip_location
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall(val_location)
zip_ref.close()


# In[ ]:



# Define directory with our training horses
train_horse_dir = os.path.join('C:\\Users\\12103\\Downloads\\horse-or-human\\horses')

# Define directory with our training humans
train_human_dir = os.path.join('C:\\Users\\12103\\Downloads\\horse-or-human\\humans')

# Define directory with our validation horses
val_horse_dir = os.path.join('C:\\Users\\12103\\Downloads\\validation-horse-or-human\\horses')

# Define directory with our validation horses
val_human_dir = os.path.join('C:\\Users\\12103\\Downloads\\validation-horse-or-human\\horses')

# Number of images in each directory
num_train_horses = len(os.listdir(train_horse_dir))
num_train_human = len(os.listdir(train_human_dir))
num_val_horses = len(os.listdir(val_horse_dir))
num_val_human = len(os.listdir(val_human_dir))

# Number of training and validation data
num_train = num_train_horses + num_train_human
num_val = num_val_horses + num_val_human

# Print the number of images in each directory
print('Total training horse images:', num_train_horses)
print('Total training human images:', num_train_human)
print('Total validation horse images:', num_val_horses)
print('Total validation human images:', num_val_human)

"""
Convolutional Neural Network
"""
# Generate model
model = keras.Sequential()

# Add the convolutional layers
for i in range(NUM_OF_CONV_LAYERS):
    # The first convoltuion layer has 16 filters
    if (i == 0):
        model.add(keras.layers.Conv2D(16, (3,3), activation = 'relu', input_shape = (300, 300, 3)))
        model.add(keras.layers.MaxPooling2D((2,2)))
    # The second convolutional layer has 32 filters
    elif (i == 1):
        model.add(keras.layers.Conv2D(32, (3,3), activation = 'relu'))
        model.add(keras.layers.MaxPooling2D((2,2)))
    # The rest of the convolutional layers have 64 filters
    else:
        model.add(keras.layers.Conv2D(64, (3,3), activation = 'relu'))
        model.add(keras.layers.MaxPooling2D((2,2)))
       
# Flatten the results to feed into deep NN
model.add(keras.layers.Flatten())

# Add the hidden layers
for i in range(NUM_OF_HIDDEN_LAYERS):
    # The first layers has 512 neurons
    if (i == 0):
        model.add(keras.layers.Dense(512, activation = 'relu'))
    # The rest of the layers has 128 neurons
    else:
        model.add(keras.layers.Dense(128, activation = 'relu'))

# Output layer (binary)
model.add(keras.layers.Dense(1, activation = 'sigmoid'))

# Summary of the model
model.summary()

# Compile the model
model.compile(loss='binary_crossentropy', optimizer = 'adam', metrics=['acc'])

# Instantiate generators and normalize the image data
train_datagen = keras.preprocessing.image.ImageDataGenerator(rescale = 1/255)
validation_datagen = keras.preprocessing.image.ImageDataGenerator(rescale = 1/255)

# Flow training images in batches of TRAIN_BATCH_SIZE
train_generator = train_datagen.flow_from_directory(
    'C:\\Users\\12103\\Downloads\\horse-or-human', # Source directory of training images
    target_size = (IMAGE_SIZE, IMAGE_SIZE),        # All the images will be resized to IMAGE_SIZE
    batch_size = TRAIN_BATCH_SIZE,
    class_mode = 'binary')                         # Binary labels

# Flow training images in batches of VAL_BATCH_SIZE
validation_generator = validation_datagen.flow_from_directory(
    'C:\\Users\\12103\\Downloads\\validation-horse-or-human', # Source directory of validation images
    target_size = (IMAGE_SIZE, IMAGE_SIZE),                  # All the images will be resized to IMAGE_SIZE
    batch_size = VAL_BATCH_SIZE,
    class_mode = 'binary')                                   # Binary labels

# Fitting the model
history = model.fit_generator(
    train_generator,
    steps_per_epoch = math.ceil(num_train / TRAIN_BATCH_SIZE),  # Take ceiling to get integer if not divisible
    epochs = 15,
    verbose = 1,
    validation_data = validation_generator,
    validation_steps = 8)   


