"""
Certainly! Here's an algorithm to get the first element from each nested list within a list in Python:

1. Start with a nested list.
2. Create an empty list to store the first elements.
3. Iterate over each sublist in the nested list.
4. For each sublist:
    * Access the first element using indexing (sublist[0]).
    * Append the first element to the list of first elements.
5. Once all sublists have been processed, the list of first elements will contain the desired values.
6. Output the list of first elements.

Here's the algorithm in a more formal format:
Algorithm to Get First Elements from Nested Lists:

Input: nested_list - a list containing nested lists

1. Let first_elements be an empty list.

2. For each sublist in nested_list, do the following:
     - Let first_element be the first element of the sublist (sublist[0]).
     - Append first_element to the list first_elements.

3. Output the list first_elements.

"""

# How to get the first element from each nested list of a list

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using a list comprehension
first_list = [element[0] for element in nested_list]
print(first_list)

# Using a for loop
my_first_list = []
for i in nested_list:
    my_first_list.append(i[0])
print(my_first_list)