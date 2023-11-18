import random
total_flips=0
for i in range(10): 
    flips=0 
    cons_count_H=0
    cons_count_T=0
    while True:
        result=random.choice(['H','T'])
        flips+=1
        if result=='H' and cons_count_H<3 and cons_count_T<3: 
            cons_count_H+=1
            cons_count_T=0
        elif result=='T'and cons_count_H<3 and cons_count_T<3:
            cons_count_T+=1
            cons_count_H=0
        print(result,end=' ')
        if cons_count_H==3 or cons_count_T==3:
            break
    total_flips+=flips
    print(f'({flips} flips)')
print(f'On average, {total_flips/10} flips were needed.')