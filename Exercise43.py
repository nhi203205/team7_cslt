a=int(input("Denomination of a banknote ($): "))
if a==1:
    print("The individual on the banknote is George Washington")
elif a==2:
    print("The individual on the banknote is Thomas Jefferson")
elif a==5:
    print("The individual on the banknote is Abraham Lincoln")
elif a==10:
    print("The individual on the banknote is Alexander Hamilton")
elif a==20:
    print("The individual on the banknote is Andrew Jackson")
elif a==50:
    print("The individual on the banknote is Ulysses S.Grant")
elif a==100:
    print("The individual on the banknote is Benjamin Franklin")
else:
    print("Error. Please try again")