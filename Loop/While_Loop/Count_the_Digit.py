n = int(input("Enter The Number: "))
count = 0
while(n>0):
    count +=1
    n = n//10
print(count)

"""for i in range(n):
    if (n > 0):
        count += 1
        n = n // 10
print(count)"""
