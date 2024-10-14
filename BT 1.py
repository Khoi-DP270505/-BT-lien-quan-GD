def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point

    for i in range(num_iterations):
        gradient = 2 * x + 6
        x = x - learning_rate * gradient
        f_x = x**2 + 6 * x + 8

        print(f"Iteration {i + 1}: x = {x}, f(x) = {f_x}")

    return x

# Ví dụ chạy thuật toán
starting_point = 0  # Điểm khởi đầu
learning_rate = 0.1  # Tốc độ học
num_iterations = 10  # Số lượng lặp

minimum = gradient_descent(starting_point, learning_rate, num_iterations)
print(f"Giá trị tối thiểu của hàm là tại x = {minimum}")
