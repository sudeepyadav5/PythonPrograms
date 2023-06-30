my_list = []
n= 5
for i in range(n):
    element = int(input(f"Enter Element {i+1}: "))
    my_list.append(element)
print(my_list)
sorting = sorted(my_list)
print(sorting[-2])
