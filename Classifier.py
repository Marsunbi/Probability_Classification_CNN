from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras import backend as keras_backend
from keras.preprocessing.image import ImageDataGenerator

image_path = R'data'
training_data_dir = R'data/training_set'
validation_data_dir = R'data/test_set'
image_width = 350
image_height = 350
shear_range = 0.2
zoom_range = 0.2
batch_size = 32
steps_per_epoch = 2000
epochs = 50
number_of_validation_samples = 1000

if keras_backend.image_data_format() == 'channels first':
    input_shape = (3, image_height, image_width)
else:
    input_shape = (image_height, image_width, 3)

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=input_shape, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=2, activation='softmax'))

model.load_weights(R'weights/weights-improvement-11-0.83-LargerSeed.hdf5')

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

