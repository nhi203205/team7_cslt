total=0
value=0
number=int(input("n="))
if number==0:
   print("Error. Please try again with another number.")
else:
    while number!=0:
        total=total+number
        value=value+1
        number=int(input("n="))
    average=total/value
    print("The average is",average)