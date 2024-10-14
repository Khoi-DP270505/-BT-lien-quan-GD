import numpy as np
import matplotlib.pyplot as plt

def gradient_descent_lr_scheduler(initial_learning_rate, decay_strategy, decay_rate, decay_steps, num_iterations, starting_point):
    x = starting_point
    learning_rate = initial_learning_rate
    history = []

    for i in range(num_iterations):
        if decay_strategy == 'step':
            if (i + 1) % decay_steps == 0:
                learning_rate *= decay_rate
        elif decay_strategy == 'exponential':
            learning_rate = initial_learning_rate * np.exp(-decay_rate * i)

        gradient = 2 * x + 6
        x = x - learning_rate * gradient
        f_x = x**2 + 6 * x + 8
        history.append(f_x)

    return history

initial_learning_rate = 0.1
decay_rate = 0.9
decay_steps = 10
num_iterations = 50
starting_point = 0

# Step Decay
step_decay_history = gradient_descent_lr_scheduler(
    initial_learning_rate=initial_learning_rate,
    decay_strategy='step',
    decay_rate=decay_rate,
    decay_steps=decay_steps,
    num_iterations=num_iterations,
    starting_point=starting_point
)

# Exponential Decay
exp_decay_history = gradient_descent_lr_scheduler(
    initial_learning_rate=initial_learning_rate,
    decay_strategy='exponential',
    decay_rate=0.05,
    decay_steps=decay_steps,
    num_iterations=num_iterations,
    starting_point=starting_point
)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_iterations + 1), step_decay_history, label='Step Decay')
plt.plot(range(1, num_iterations + 1), exp_decay_history, label='Exponential Decay')
plt.xlabel('Iteration')
plt.ylabel('f(x)')
plt.title('Gradient Descent with Learning Rate Scheduler')
plt.legend()
plt.grid()
plt.show()
