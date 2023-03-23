a=int(input("Enter the first side of the triangle "))
b=int(input("Enter the second side of the triangle "))
c=int(input("Enter the third side of the triangle "))
if(a==b and a==c):
    print("Equilateral")
elif(a==b or a==c or b==c):
    print("Isoceles")
else:
    print("Scalene")