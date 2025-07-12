#recursive non memo (rekursif biasa)
def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get user input
num = int(input("Enter a positive integer: "))

# Calculate and print Fibonacci number
print(f"Fibonacci({num}) = {fibonacci(num)}")



#recursive memo
# import time

# def fib_memo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
#     return memo[n]

# # Get user input
# n = int(input("Enter Fibonacci number: "))

# # Measure execution time
# start = time.perf_counter()
# result = fib_memo(n)
# end = time.perf_counter()

# # Print the result and execution time
# print(f"fib({n}) = {result}")
# print(f"Memoized recursion took: {end - start:.6f} seconds")

