print("Triangle sides:")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a==b==c:
    type="Equilateral"
elif a==b or a==c or b==c:
    type="Isosceles"
else:
    type="Scalene"
print("Type of triangle:",type)