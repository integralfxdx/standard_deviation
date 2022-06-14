def result():
    from math import sqrt,pow
    combine=list(map(int,input("combine number : ").split(' ')))
    std_mean=0
    mean=0
    S=0

    for h in range(0,len(combine)):
        S+=combine[h]

    mean=S/len(combine)

    for s in range(0,len(combine)):
        std_mean+=pow((combine[s]-mean),2)
    standard_mean=sqrt((std_mean)/len(combine))

    print("sum : ",S)
    print("mean : ",mean)
    print("std_mean : %.2f" % standard_mean)
result()