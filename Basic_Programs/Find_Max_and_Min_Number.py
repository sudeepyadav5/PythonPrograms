size_of_listing = int(input("Enter the Size of Listing : "))
collect_list = []
for i in range(size_of_listing):
    user_input = int(input("Enter Input: "))
    collect_list.append(user_input)
print("My List", collect_list)
print("Mix List", max(collect_list))
print("Min List", min(collect_list))