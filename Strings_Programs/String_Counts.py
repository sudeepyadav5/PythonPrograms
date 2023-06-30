my_string = "Sudeep"
my_dict = {}

for char in my_string:
    if char in my_dict:
        my_dict[char]+=1
    else:
        my_dict[char] = 1

print(my_dict)


