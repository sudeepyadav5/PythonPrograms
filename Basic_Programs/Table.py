user_table = int(input("Enter Table Number: "))
a = 10
Table = 1

for i in range(1,a+1):
    if user_table != 0:
        Table = i * user_table
        print(f"{user_table} * {i} = {Table}")
