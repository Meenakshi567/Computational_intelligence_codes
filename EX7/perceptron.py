import math

# Initial values
w1 = 0.3
w2 = -0.2
bias = 0.4
learning_rate = 0.2

# Training data
training_data = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

# -------- USER INPUT --------
epochs = int(input("Enter number of epochs: "))

print("Choose Activation Function:")
print("1. Step Function")
print("2. Sigmoid Function")
choice = int(input("Enter choice (1/2): "))

# -------- ACTIVATION FUNCTIONS --------
def step_function(x):
    return 1 if x >= 0.5 else 0

def sigmoid_function(x):
    return 1 if (1 / (1 + math.exp(-x))) >= 0.5 else 0

# Select activation function
if choice == 1:
    activation = step_function
elif choice == 2:
    activation = sigmoid_function
else:
    print("Invalid choice! Defaulting to Step Function.")
    activation = step_function

# -------- TRAINING --------
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}")
    print("---------------------------------------------------------------")
    print("X1  X2  Target   Yin      Y    W1      W2      Bias")
    print("---------------------------------------------------------------")

    for inputs, target in training_data:
        x1, x2 = inputs

        # Net input
        yin = (x1 * w1) + (x2 * w2) + bias

        # Output
        y = activation(yin)

        # Error
        error = target - y

        # Update weights and bias
        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        bias = bias + learning_rate * error

        # Print row
        print(f"{x1:<3} {x2:<3} {target:<7} {yin:<8.2f} {y:<5} {w1:<8.2f} {w2:<8.2f} {bias:<8.2f}")

print("\nFinal Weights:")
print(f"W1 = {w1:.2f}, W2 = {w2:.2f}, Bias = {bias:.2f}")