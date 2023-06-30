# How to reverse the List using slice
num = int(input("Enter Range of List: "))
my_list = []
for i in range(num):
    element = int(input("Enter Element: "))
    my_list.append(element)
print("Original  List", my_list)
reverse = my_list[::-1]
print("Reverse List", reverse)


