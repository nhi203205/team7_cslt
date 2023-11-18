import math
x=input('Enter the x part of the coordinate: ')
Totalx=0
Totaly=0
while x=='':
    break
while x!='':
    y=input('Enter the y part of the coordinate: ')
    Totaly=Totaly + float(y)
    Totalx=Totalx + float(x)
    x=input('Enter the x part of the coordinate: ')
z=math.sqrt((Totalx)**2+(Totaly)**2)
t=(Totalx)+(Totaly)+z
print('The perimeter of that polygon is',t)