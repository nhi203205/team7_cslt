number=int(input("Enter an integer: "))
result=""
q=number
while q>0:
    r=q%2
    result=str(r)+result
    q=q//2
print("The binary number of",number,"is",result)