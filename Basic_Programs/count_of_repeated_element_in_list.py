# How to count occurrence of repeated element in list

from collections import Counter

my_list = [15, 18, 14, 'C#', 18, 15, 'C#', 'C++', 'C++', 'Python', 15]

repeation_of_element = Counter(my_list)
print(repeation_of_element)
# if repeation_of_element == 1:
#     print(repeation_of_element)
# else:
#     pass