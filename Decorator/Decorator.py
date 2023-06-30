def sum_decorator(func):
    def wrapper(a, b):
        print("Calculating the sum...")
        return func(a, b)

    return wrapper


@sum_decorator
def sum_numbers(a, b):
    return a + b


result = sum_numbers(5, 7)
print("Result:", result)
