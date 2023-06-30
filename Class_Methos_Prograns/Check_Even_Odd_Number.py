class Number:
    @classmethod
    def check_odd_even(cls, num):
        if num % 2 == 0:
            return f"{num} is even."
        else:
            return f"{num} is odd."


# Prompt the user for the size of the list
size = int(input("Enter the size of the list: "))

# Prompt the user to enter the elements of the list
elements = []
for i in range(size):
    num = int(input(f"Enter element {i + 1}: "))
    elements.append(num)

# Check whether each element is odd or even using the class method
for element in elements:
    print(Number.check_odd_even(element))

