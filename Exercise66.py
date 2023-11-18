i=0
total=0
while True:
    lg=input("Enter letter grades: ")
    if lg=="A" or lg=="A+":
        gp=4
    elif lg=="A-":
        gp=3.7
    elif lg=="B+":
        gp=3.3
    elif lg=="B":
        gp=3.0
    elif lg=="B-":
        gp=2.7
    elif lg=="C+":
        gp=2.3
    elif lg=="C":
        gp=2.0
    elif lg=="C-":
        gp=1.7
    elif lg=="D+":
        gp=1.3
    elif lg=="D":
        gp=1.0
    elif lg=="F":
        gp=0
    elif lg=="":
        break
    total=total+gp
    i=i+1
    average=total/i
print("Grade point average is",average)