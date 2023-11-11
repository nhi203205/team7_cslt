a=int(input("Day: "))
b=int(input("Month: "))
if a==1 and b==1:
    print("New Year's Day")
elif a==1 and b==7:
    print("Canada Day")
elif a==25 and b==12:
    print("Christmas Day")
else:
    print("Not compatible with any holidays")
