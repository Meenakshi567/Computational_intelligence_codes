import math

# -------- USER INPUT --------

# Number of inputs
n = int(input("Enter number of input features: "))

# Initial weights
weights = []
for i in range(n):
    w = float(input(f"Enter initial weight w{i+1}: "))
    weights.append(w)

# Bias
bias = float(input("Enter initial bias: "))

# Learning rate
learning_rate = float(input("Enter learning rate: "))

# Number of epochs
epochs = int(input("Enter number of epochs: "))

# Number of training samples
num_samples = int(input("Enter number of training samples: "))

# Training data input
training_data = []
print("\nNOTE: For Bipolar, use 1 and -1.")
for i in range(num_samples):
    print(f"\nSample {i+1}:")
    # Taking inputs as float, but user should provide 1.0 or -1.0
    inputs = list(map(float, input(f"Enter {n} inputs (space-separated): ").split()))
    target = int(input("Enter target (1/-1): "))
    training_data.append((inputs, target))

# -------- BIPOLAR ACTIVATION FUNCTIONS --------
print("\nChoose Activation Function:")
print("1. Bipolar Step Function (Threshold = 0)")
print("2. Bipolar Sigmoid Function")
choice = int(input("Enter choice (1/2): "))

def bipolar_step_function(x):
    # Standard Bipolar Step: 1 if x >= 0, else -1
    return 1 if x >= 0 else -1

def bipolar_sigmoid_function(x):
    # Mapping Sigmoid (0 to 1) to Bipolar (-1 to 1)
    # Threshold at 0.5 for sigmoid is equivalent to 0 for bipolar
    sigmoid_val = 1 / (1 + math.exp(-x))
    return 1 if sigmoid_val >= 0.5 else -1

# Select activation
if choice == 1:
    activation = bipolar_step_function
elif choice == 2:
    activation = bipolar_sigmoid_function
else:
    print("Invalid choice! Defaulting to Bipolar Step Function.")
    activation = bipolar_step_function

# -------- TRAINING --------
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}")
    print("-------------------------------------------------------------------")
    print("Inputs              Target   Yin      Y    Updated Weights        Bias")
    print("-------------------------------------------------------------------")

    all_correct = True # To check for convergence

    for inputs, target in training_data:

        # Net input calculation
        yin = sum(x * w for x, w in zip(inputs, weights)) + bias

        # Output calculation
        y = activation(yin)

        # Error (Target - Actual)
        error = target - y

        if error != 0:
            all_correct = False
            # Update weights: w(new) = w(old) + alpha * error * x
            # Note: In some bipolar literature, error is treated as 2 or -2
            # This standard perceptron rule handles it correctly.
            for i in range(n):
                weights[i] = weights[i] + learning_rate * error * inputs[i]

            # Update bias
            bias = bias + learning_rate * error

        # Format inputs and weights for clean display
        input_str = str(inputs)
        formatted_weights = " ".join([f"{w:.2f}" for w in weights])

        # Print row
        print(f"{input_str:<18} {target:<7} {yin:<8.2f} {y:<5} {formatted_weights:<20} {bias:.2f}")

    if all_correct:
        print("\nConvergence reached! All targets match outputs.")
        break

# -------- FINAL OUTPUT --------
print("\nFinal Weights and Bias:")
for i in range(n):
    print(f"W{i+1} = {weights[i]:.2f}")
print(f"Bias = {bias:.2f}")