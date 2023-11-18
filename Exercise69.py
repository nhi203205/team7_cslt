pi=0
for i in range(15):
    if i==0:
        pi=pi+3
    else:
        num=(-1)**(i+1)
        d=2*i
        den=d*(d+1)*(d+2)
        pi=pi+num*(4/den)
    print(pi)