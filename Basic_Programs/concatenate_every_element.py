str1 = ["A","B","C"]
str2 = ["D","E","F"]

# str1.extend(str2)
# print(str1)


# How to concatenate every element across lists using list comprehension
temp = [(x,y) for x in str1 for y in str2]
concat_list = [x + '' + y for (x,y) in temp]
print(concat_list)