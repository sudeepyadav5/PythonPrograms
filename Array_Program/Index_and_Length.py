"""Problem 1: Array Problem based on Index and Length
Given an array of integers and an index, write a Python program to find the value at the specified index. If the index is out of bounds (either less than 0 or greater than or equal to the array length), return "Index out of bounds."
"""


def find_value_at_index(arr, index):
    if index < 0 or index >= len(arr):
        return "Index out of bounds."

    return arr[index]


# Example usage
array = []
for i in range(5):
    element = int(input(f"Enter Array Element of {i}: "))
    array.append(element)
index = int(input("Enter Index value: "))
# array = [1, 5, 9, 3, 7]
# index = 2
result = find_value_at_index(array, index)
print(f"The value at index {index} is: {result}")
