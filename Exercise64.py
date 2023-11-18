S=0
while True:
    n=input('Price of the item: ')
    if not n:
        break
    n=float(n)
    S+=n
e=S
if e%5<2.5:
    e=e-(e%5)
else:
    e=e+(5-(e%5))
print('The cost of all items is:',round(S,1))
print('The amount to be paid is:',e)