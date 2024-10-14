import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    history = []

    for i in range(num_iterations):
        gradient = 2 * x + 6
        x = x - learning_rate * gradient
        f_x = x**2 + 6 * x + 8
        history.append(f_x)

    return history

learning_rates = [0.001, 0.01, 0.1, 1.0]
starting_point = 0
num_iterations = 50

plt.figure(figsize=(10, 6))

for lr in learning_rates:
    history = gradient_descent(starting_point, lr, num_iterations)
    plt.plot(range(1, num_iterations + 1), history, label=f'Learning rate: {lr}')

plt.xlabel('Iteration')
plt.ylabel('f(x)')
plt.title('Gradient Descent Convergence for Different Learning Rates')
plt.legend()
plt.grid()
plt.show()
