import random
x = random.randint(1,100)
n = 1
count = 0
max = x
print(x,end='\n')
while n<=100:
  x = random.randint(1,100)
  print(x,end='\n')
  if max < x:
    max = x
    count+=1
  n+=1
print('The maximum value found was',max,end = '\n')
print('The maximum value was updated',count,'times')