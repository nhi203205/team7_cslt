m=int(input("Positive integer 1: "))
n=int(input("Positive integer 2: "))
d=min(m,n)
if m>0 and n>0:
    while m%d!=0 or n%d!=0:
        d=d-1  
    print("The greatest common divisor of n and m is",d)