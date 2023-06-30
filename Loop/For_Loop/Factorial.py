n = int(input("Enter N Number: "))
f = 1
if (n>0):
    for i in range(1, n+1):
        f = f*i
    print(f"Factorial of {n}! is {f}")
else:
    print("N Value Should be Non- Negative value")
