
'''
Using TensorFlow in Python involves several steps, including installation, importing necessary modules, building and training models, and evaluating or deploying them. Here's a basic guide:

1. Installation:
You can install TensorFlow using pip:
    pip install tensorflow
If you have a GPU, you might want to install TensorFlow with GPU support for faster computations:
    pip install tensorflow-gpu
2. Importing TensorFlow:
3. Building a Simple Neural Network:
4. Loading Data:
5. Training the Model:
6. Evaluation:
7. Making Predictions:
8. Saving and Loading Models:
9. Using TensorFlow with GPU: If you have a GPU and installed TensorFlow with GPU support, TensorFlow will automatically use it for computation. You can verify GPU usage with the following code:
10. TensorFlow with Eager Execution: By default, TensorFlow 2.x uses eager execution, which evaluates operations immediately. This makes TensorFlow behave more like Python, but it's still possible 
    to use graph execution for better performance:
This is a basic outline of using TensorFlow in Python. TensorFlow provides many more features, such as custom layers, callbacks, and more, 
for building complex neural networks and machine learning models.

'''
import tensorflow as tf

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Load your dataset, for example, MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0


# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Make predictions
predictions = model.predict(x_test)

# Save the model
model.save('my_model.h5')

# Load the model
loaded_model = tf.keras.models.load_model('my_model.h5')

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))


tf.config.run_functions_eagerly(False)








