# def fibonacci(n):
#     fib_series = [0, 1]  # Initial values of the series
#     if n <= 0:
#         return "Invalid input. Please enter a positive integer."
#     elif n == 1:
#         return fib_series[:1]
#     elif n == 2:
#         return fib_series
#
#     while len(fib_series) < n:
#         next_number = fib_series[-1] + fib_series[-2]  # Compute the next number in the series
#         fib_series.append(next_number)
#
#     return fib_series
#
# # Example usage
# num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
# series = fibonacci(num_terms)
# print("Fibonacci series:", series)

num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Check if the input is valid
if num_terms <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    fib_series = [0, 1]  # Initialize the series with the first two values

    # Generate the series
    if num_terms == 1:
        print(fib_series[:1])
    elif num_terms == 2:
        print(fib_series)
    else:
        while len(fib_series) < num_terms:
            next_number = fib_series[-1] + fib_series[-2]  # Compute the next number
            fib_series.append(next_number)

        print("Fibonacci series:", fib_series)
