# How to Intersect two list
AList = []
BList = []
for i in range(4):
    A = input(f"Enter Value of A{i+1}: ")
    AList.append(A)
print(f"List of A {AList} \n")

for j in range(4):
    B = input(f"Enter Value of  B{j+1}: ")
    BList.append(B)
print("List of B ", BList)

intersection = list(set(AList).intersection(BList))
print("\n A Intersection B is ",intersection)

unionsection = list(set(AList).union(BList))
print("\n A Union-section B is ",unionsection)

"""intersect = [item for item in AList if item in BList]
print("intersect of two list", intersect)"""
"""
listnum = ['C++',2,3,6,7,5,'C#']
listnum1 = ['C++',5,6,7,'C#']
 
intersect_res = [item for item in listnum if item in listnum1]
 
print('intersect of two list =',intersect_res)
"""



