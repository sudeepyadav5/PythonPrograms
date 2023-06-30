"""Question :- You'd like to know how many triangles can be formed with side lengths equal to adjacent
               'elements from arr.Construct an array of integers of length arr.length - 2, where
               the ith element is equal to 1 if it's possible to form a triangle with side lengths
               arr [i], arr [i + 1], and arr [i + 2], otherwise 0.Return the resulting array of integers.
               Note: A triangle can be formed with side lengths a, b, and c if a + b > c, a + c > b, and
               b + c > a.ExampleFor arr = [1, 2, 2, 4], the output should be canMakeTriangle (arr) = [1, 0].
               output = 1 because we can form a triangle with side lengths 1, 2, and 2."""

"""
To solve this problem, we can iterate over the array arr from the beginning to the third-to-last element. 
For each index i, we check if it is possible to form a triangle using the side lengths arr[i], arr[i + 1],
 and arr[i + 2] according to the triangle inequality theorem.

Here's the algorithm to solve this problem:
1. Initialize an empty list result to store the output.
2. Iterate over i from 0 to len(arr) - 3 (inclusive).
        If arr[i] + arr[i + 1] > arr[i + 2], append 1 to result (triangle can be formed).
        Otherwise, append 0 to result (triangle cannot be formed).
3. Return the result list.
"""


def canMakeTriangle(arr):
    result = []
    for i in range(len(arr) - 2):
        if arr[i] + arr[i + 1] > arr[i + 2]:
            result.append(1)
        else:
            result.append(0)
    return result


n = 4
arr = []
for k in range(n):
    element = int(input(f"Enter Element {k + 1}: "))
    arr.append(element)

print(canMakeTriangle(arr))  # Output: [1, 0]
