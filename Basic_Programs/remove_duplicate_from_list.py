my_list = [12, 36, 56, 36, 36, 50, 56, 12]
unique_list_by_set = list(set(my_list))
print(unique_list_by_set)

my_list1 = [12, 36, 56, 36, 36, 50, 56, 12]
unique_list_by_dict = list(dict.fromkeys(my_list1))
print(unique_list_by_dict)

# remove duplicates from a list using list comprehension in Python
my_lists = [1, 2, 3, 3, 4, 5, 5, 6]
unique_list = []

[unique_list.append(x) for x in my_lists if x not in unique_list]

print(unique_list)


