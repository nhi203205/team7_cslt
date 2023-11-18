n=int(input("Enter an integer: "))
if n<2:
    print("The entered value should be greater than or equal to 2.")
else:
    j=2
    while j<=n:
        if n%j==0:
            print(j)
            n=n//j
        else:
            j=j+1