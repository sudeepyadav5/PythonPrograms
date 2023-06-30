"""def find_second_max(numbers):
    max_num = float('-inf')
    second_max = float('-inf')

    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num

    return second_max

# Example usage:
num_list = [3, 7, 2, 8, 4, 5]
result = find_second_max(num_list)
print("The second maximum number is:", result)"""

# Python program to find second largest
# number in a list

# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

# mx = max(list1[0], list1[1])
# secondmax = min(list1[0], list1[1])
mx = max(list1)
secondmax = min(list1)
n = len(list1)
for i in range(0, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and secondmax != list1[i]:
        secondmax = list1[i]

print("Second highest number is : ", str(secondmax))
