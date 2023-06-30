def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["price"] < right[j]["price"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
products = [
    {"name": "Product 1", "price": 25.99},
    {"name": "Product 2", "price": 10.99},
    {"name": "Product 3", "price": 49.99},
    {"name": "Product 4", "price": 5.99},
    {"name": "Product 5", "price": 35.99}
]

sorted_products = merge_sort(products)

# Print sorted products
for product in sorted_products:
    print(product["name"], "-", product["price"])
