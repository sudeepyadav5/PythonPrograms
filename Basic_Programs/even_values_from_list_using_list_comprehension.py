# How to Filter even values from a list using list comprehension

my_list = [12, 18, 14, 18, 15, 6, 1, 3]

even_list = [ele for ele in my_list if ele % 2 == 0]
odd_list = [ele for ele in my_list if ele % 2 != 0]
print("My Even Number is ", even_list)
print("My Odd Number is ", odd_list)
