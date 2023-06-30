def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# Example usage
size = int(input("Enter the Size of Element: "))
numbers = []
for i in range(size):
    element = int(input(f"Enter Element {i+1}: "))
    numbers.append(element)
print("List for Searching is ", numbers)
target = int(input("Enter Search Element: "))

index = binary_search(numbers, target)

if index != -1:
    print(f"Found {target} at index {index+1}.")
else:
    print(f"{target} not found in the list.")
