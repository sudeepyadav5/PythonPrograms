# How to remove negative values from a list with the filter function

my_list = [-5, 27, 1000, -4, 0, -80,56,-67]
positive_value = []
for i in my_list:
    if i >=0:
        positive_value.append(i)
print(positive_value)

"""OR
lstnum = [-5, 27, 1000, -4, 0, -80,56,-67]
//Removing negative values
res_lst = [item for item in lstnum if item >= 0] 
print('list after removing negative values =',res_lst)"""
