print("*-*Temperature conversion table*-*")
print("|-------------------------------|")
print("|    Celsius    |   Fahrenheit  |")
print("|---------------|---------------|")
for i in range(101):
    if i%10==0:
        F= i*(9/5) + 32
        print("|\t",i,"\t|\t ",int(F),"\t|")
print("|---------------|---------------|")