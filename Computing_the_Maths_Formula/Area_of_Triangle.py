# Area of Triangle using formula
# area = sqrt(s*(s-a)*(s-b)*(s-c)
# )

a = float(input("Enter the First Side of the Triangle: "))
b = float(input("Enter the Second Side of the Triangle: "))
c = float(input("Enter the Third Side of the Triangle: "))
s = (a*b*c)/2
print(f"S = {s}")
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Triangle is = : ", area)