import time

def fib_loop(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# Get user input
n = int(input("Enter Fibonacci number: "))

# Measure execution time
start = time.perf_counter()
result = fib_loop(n)
end = time.perf_counter()

# Print the result and execution time
print(f"fib({n}) = {result}")
print(f"Loop-based Fibonacci took: {end - start:.6f} seconds")
