"""# Program to find the sum of list elements.
size_list = int(input("Enter Size of List: "))
my_list = []
sum = 0
for i in range(size_list):
    element = int(input("Enter the List Element: "))
    my_list.append(element)
# print("My Element List", my_list)
for j in range(0, len(my_list)):
    sum = sum + my_list[j]
print(f"Sum of List {my_list} is {sum}")

"""
my_list = [2,3,5,40]
sum = 0
for j in range(len(my_list)):
    sum = sum + my_list[j]
print(f"Sum of List {my_list} is {sum}")